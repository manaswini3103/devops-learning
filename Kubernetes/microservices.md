# Microservices Architecture

- We will understand microservices architecture using a simple web application developed by Docker and deploy this application on multiple different Kubernetes platforms such as Google Cloud Platform.
- Lets take a sample voting application which provides an interface for a user to vote, and another interface to show the results.
- The architecture and data flow of this simple voting application stack is like below:
  - voting app (web application developed in Python, listens on port **80**) provides user interface to choose between two options a cat and a dog.
  - The vote is stored in redis (serves as a database in memory, listens on port **6, 3, 7, 9**).
  - This vote is then processed by the worker (application written in dotnet).
  - worker takes new vote and updates the Postgres SQL database (here it is a table with the number of votes for Cats and dogs, listens on port **5432**).
  - Finally, the result app (web application developed in Node.js, listens on port **80**) is displayed in a web interface, which reads the count of votes from the Postgres SQL database and displays it to the user.
- We can put together this application stack on a single Docker engine using Docker run commands.
- Lets assume that all images of applications are already built and are available on Docker repository.
  - **docker run -d --name=redis redis** (starts an instance of redis image, -d: runs container in background)
  - **docker run -d --name=db postgres:9.4** (deploying a postgres database)
  - **docker run -d --name=vote -p 5000:80 --link redis:redis voting-app** (5000 is port on host, 80 is port, image is voting-app, as voting-app is dependent on redis we add link option NameOfContainer:NameOfHost. It creates a entry in /etc/hosts with host name and internal IP of this container, and we are naming the instance as 'vote')
  - **docler run -d --name=result -p 5001:80 --link db:db result-app** (publish port 80 to port 5001 on host, we are linking the db to result as it is dependent on that.)
  - **docker run -d --name=worker --link redis:redis --link db:db worker** (worker requires both SQL and redis)
- **Link** is a command line option which can be used to link two containers together.



# Deploying Voting-App on Kubernetes
We saw how the voting application works on Docker, now we'll deploy it on Kubernetes.

## Goals
- Deploy Containers on a Kubernetes cluster
- Enable Connectivity between containers, so they can access each other and alog with the databases
- External Access for external facing applications like voting and result app
## Steps
- Deploy these applications as a pod/replica sets/deployments on our Kubernetes cluster
- create services (Cluster IP) : redis, db
- create services (Node Port) : voting-app, result-app
## Images
These images are built from a fork of the original project developed in the Docker Samples repository. And for the databases we will use the official Redis and PostgreSQL releases that are available.
- voting-app: kodekloud/examplevoting-app_vote:v1
- redis: redis
- postgres: postgressql
- result-app: kodekloud/examplevotingapp_result:v1

- So once the pods are deployed the next step is to enable connectivity between the services.
- Note that the worker app is not being accessed by anyone. It simply reads the count of votes from the database, and then updates the total count of votes on the Postgres SQL database. It has no service because it's just a worker, and it's not accessed by any other service or external users.
- How can you make one component accessible by another?
  - For example, how can we make the Redice database accessible by the voting app? Should the voting app use the IP address of the Redis pod?
  - No, becuase the IP of pod can change if the pod restarts. And we may also run into issues when you try to scale your applications in the future.
  - The right way to do it is to use a service. service can be used to expose an application to other applications or users for external access.
- So we will create a service for the Redis pod to be accessed by voting app and worker app. And call it a Redis service, and it will be accessible anywhere within the cluster it's name.
- It's important to name your service Redis so that these applications can connect to the database. It is not best practice, to hard code stuff like this within the source code Instead we should use environment variables.
-	These services are not to be accessed outside the cluster. So, type is ‘cluster IP’.
-	We will follow the same approach of creating a service for the PostgreSQL pod, so that the PostgreSQL DB can be accessed by the worker and the result app.
-	While connecting to DB, the worker and result apps are passing a username and password, both of which are set to Postgres.
-	We need external access for voting and result app. So, we create ‘node port’ service. We would use a port number greater than 30,000 to make them available.
-	‘worker’ process reads from one database and updates another and we don’t need a service for it. As a service is only required if the application has some kind of process or database service or web service that needs to be exposed, that needs to be accessed by others.

### Pod Definition Files
**voting-app-pod.yaml**  
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: vote
  labels:
    app: vote
spec:
  containers:
  - name: vote
    image: dockersamples/examplevotingapp_vote
    ports:
      - containerport: 80
        name: vote
```

**result-app-pod.yaml**  
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: result
  labels:
    app: result
spec:
  containers:
  - name: result
    image: dockersamples/examplevotingapp_result
    ports:
      - containerport: 80
        name: result
```

**redis-pod.yaml**  
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: redis
  labels:
    app: redis
spec:
  containers:
  - name: redis
    image: redis:alpine
    ports:
      - containerport: 6379
        name: redis
```

**db-pod.yaml**
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: db
  labels:
    app: db
spec:
  containers:
  - name: postgres
    image: postgres:15-alpine
    env:
      - name: POSTGRES_USER
        value: postgres
      - name: POSTGRES_PASSWORD
        value: postgres
    ports:
      - containerport: 5432
        name: postgres
```

**worker-pod.yaml**
```YAML
apiVersion: v1
kind: Pod
metadata:
  name: worker
  labels:
    app: worker
spec:
  containers:
  - name: worker
    image: dockersamples/examplevotingapp_worker
```

### Service Definition Files 
**redis-service.yaml**  
```YAML
apiVersion: v1
kind: Service
metadata:
  name: redis
  labels:
    app: redis
spec:
  type: ClusterIP
  ports:
  - name: “redis-service”
    port: 6379
    targetport: 6379
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    app: redis
```

**db-service.yaml**  
```YAML
apiVersion: v1
kind: Service
metadata:
  name: db
  labels:
    app: db
spec:
  type: ClusterIP
  ports:
  - name: “db-service”
    port: 5432
    targetport: 5432
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    app: db
```

**voting-service.yaml**  
```YAML
apiVersion: v1
kind: Service
metadata:
  name: vote
  labels:
    app: vote
spec:
  type: NodePort
  ports:
  - name: “vote-service”
    port: 8080 # we can access this port, which in turn will access targetport
    targetport: 80
    nodePort: 31000
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    app: vote
```

**result-service.yaml**  
```YAML
apiVersion: v1
kind: Service
metadata:
  name: result
  labels:
    app: result
spec:
  type: NodePort
  ports:
  - name: “result-service”
    port: 8081 # we can access this port, which in turn will access targetport
    targetport: 80
    nodePort: 31001
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    app: result
```

-	We need to set up the node and then run this command **Kubectl apply -f .**, creates all the pods and services in present working directory, otherwise we can even run one at a time like **kubectl apply -f db-pod.yaml**.
-	Now we could see all the pods and services by giving **kubectl get pods**, **kubectl get svc**
-	So we deployed all of the pod specifications, as well as the specifications for the different services,
-	so that they can all communicate with one another.
-	And the voting application and the result application were exposed to the outside world using the Nodeport
-	service.
-	Now, since we deployed pods directly, I want you guys to be aware that there are some limitations
-	when you deploy pods directly.
-	One there isn't a way to easily scale up the number of pods, so if we wanted instead of one instance
-	of the voting app, we wanted five.
-	It doesn't provide us a mechanism to easily scale up and scale down.
-	On top of that, if one of our applications goes down, there's nothing watching over it to restart
-	it or deploy a new instance.
-	You don't get that functionality with just pods.
-	And on top of that, there's no simple way to upgrade your application.
-	So if you want version two of the voting or result app, you would have to delete the old one.
-	Deploy a brand new pod spec with the new version, and this could lead to user impact as your service
-	would be down during that time.
-	So instead of deploying pods directly, what we want to do is we want to make use of other Kubernetes
-	primitives like replica sets and deployments.
-	More specifically, we're going to be focusing on using deployments because deployments help address
-	a lot of these concerns.
-	So instead of deploying each one of these components as a pod, we're going to deploy it as a deployment.
-	This is going to give us a lot of extra benefits.
-	Like it's very easy to scale up and scale down.
-	It's going to give us the ability to monitor and watch our pods.
-	So if one pod goes down, the deployment will create a new one, and you'll see that it's very easy
-	to deploy new versions of your application as it has built in rolling update functionality so your users
-	aren't impacted.
-	And we're going to be using deployments because instead of replica sets, deployments actually use replica
-	sets under the hood.
-	So we're going to be using deployments which are an abstraction over pods and replica sets themselves.
-	We’ll delete everything by giving **kubectl delete -f .**, we’ll create a new folder called deployments and create a file called

### Deployment Definition Files
**vote-deployment.yaml**  
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vote
  labels:
    app: vote
spec:
  replicas: 1
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    matchLabels:    
      app: vote
  template: # take the template section from vote-pod.yaml
    metadata:
      name: vote
      labels:
        app: vote
    spec:
    containers:
     - name: vote
       image: dockersamples/examplevotingapp_vote
       ports:
         - containerPort: 80
           name: vote
```

**result-deployment.yaml** 
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: result
  labels:
    app: result
spec:
  replicas: 1
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    matchLabels:    
      app: result
  template: # take the template section from vote-pod.yaml
    metadata:
      name: result
      labels:
        app: result
    spec:
      containers:
        - name: result
          image: dockersamples/examplevotingapp_result
          ports:
            - containerPort: 80
              name: result
```

**redis-deployment.yaml**  
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  labels:
    app: redis
spec:
  replicas: 1
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    matchLabels:    
      app: redis
  template: # take the template section from vote-pod.yaml
    metadata:
      name: redis
      labels:
        app: redis
    spec:
      containers:
        - name: redis
          image: redis:alpine
          ports:
            - containerPort: 6379
              name: redis
```

**db-deployment.yaml**  
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db
  labels:
    app: db
spec:
  replicas: 1
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    matchLabels:    
      app: db
  template: # take the template section from vote-pod.yaml
    metadata:
      name: db
      labels:
        app: db
    spec:
      containers:
        - name: postgres
          image: postgres:15-alpine
          env:
            - name: POSTGRES_USER
              value: postgres
                  - name: POSTGRES_PASSWORD
                    Value: postgres
                ports:
            - containerPort: 5432
              name: postgres
```

**Worker-deployment.yaml**  
```YAML
db-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: worker
  labels:
    app: worker
spec:
  replicas: 1
  selector:  # what pods should it forward the traffic to, grab labels from redis_pod
    matchLabels:    
      app: worker
  template: # take the template section from vote-pod.yaml
    metadata:
      name: worker
      labels:
        app: worker
    spec:
      containers:
        - name: worker
          image: dockersamples/examplevotingapp_worker
```

-	We’ll not change anything with the services
-	Then we’ll deploy the deployments
**kubectl apply -f .**, **kubectl get svc**, **kubectl get deployment**, as deployments use replica sets, we can list them **kubectl get rs** or we can give **kubectl get all** then we’ll get everything
-	Then run **kubectl get node -o wode** and **kubectl get pode -o wide**, take the IP of the node along with the port (31000) of voting app from services and give it in browser, then we’ll be able to access it.
-	How can we scale the number of pods for deployment  
If we want to increase the number of instances for voting app run  
**kubectl scale deployment vote –replicas=5**


# Deploying Kubernetes on Cloud
For production purposes, there are many ways to get started with Kubernetes cluster, both in a private or a public cloud environment. 

Self-Hosted/Turnkey Solutions
-	We provision VMs
-	We configure VMs
-	We use some tools or scripts to deploy clusters and maintain VMs ourselves
-	Provisioning the cluster itself and managing the lifecycle of the cluster are mostly made easy using certain tools and scripts
-	Ex: Deploying Kubernetes cluster on AWS using kops or KubeOne

Hosted Solutions (Managed Solutions)
-	Kubernetes-as-a-service where the cluster along with required VMs are deployed by the Provider and Kubernetes is configured by the Provider
-	Provider provisions VMs
-	Provider installs Kubernetes
-	provider maintains VMs
-	version of Kubernetes and master nodes are all managed by the Provider.
-	Ex: Google Container/Kubernetes Engine (GKE) provisions Kubernetes cluster in some minutes with few clicks, without having to perform any kind of configuration by us.

We’ll deploy voting application on GKE, Azure Kubernetes Service (AKS), Amazon Elastic Kubernetes Service (EKS)


## Deploying on AKS
-	Open Azure, we need to have an account and then open AKS, then we need to add a Kubernetes Cluster by clicking on Add+, which will take us to the ‘Create Kubernetes Cluster Screen’
-	In Basics tab: Our subscription will be selected by default; we’ll create a resource group named ‘votingapp-resourcegroup’ then we could name the cluster as ‘example-voting-app’.
-	Cross check the region, Kubernetes version would be some default value. And set the node count to 1.
-	There are some other tabs as well, but we’ll leave them as is. And click on ‘review and create’ button. Then a new tab will open named ‘review+create’ then click on create. 
-	Then it’ll first initialize the resource group, then it’ll create the Kubernetes cluster.
-	Once it’s created, we’ll search for the name that we have to our cluster, which is ‘example-voting-app’.
-	And to access the cluster we will make use of the cloud shell uh which will open in the lower half of the screen. Which will be in black tool bar beside the icon settings.
-	It’ll ask for ‘create storage’, click on it and wait for it to complete
-	We could click on this link Quickstart: Deploy an Azure Kubernetes Service (AKS) cluster using the Azure portal - Azure Kubernetes Service | Microsoft Learn for clear details.
-	To set up the kube config (to be able to use kubectl) we need to give the below command in the cloud shell **az aks get-credentials --resource-group myResourceGroup --name myAKSCluster**, but we need to replace the name of the resource group and name of the cluster. ** az aks get-credentials --resource-group votingapp-resourcegroup --name example-voting-app**
-	Then we’ll check for the nodes **kubectl get nodes** and we’ll clone the got repo which has voting app deployments and services in it **git clone https://github.com/kodekloudhub/example-voting-app.git**
-	Then we’ll go to the directory **cd example-voting-app/k8s-specifications/**
-	Then we’ll create the services and deployments **kubectl create -f .**, then check the status of them **kubectl get deployments, svc**
-	We’ll use external IP of both voting and result app in new browser, then we can access them.
