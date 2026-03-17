# Deployment

- Pods deploy single instances of our application; multiple such pods are deployed using replication controllers or replica sets. And then comes **Deployment**, which is a Kubernetes object that comes higher in the hierarchy.
- The Deployment provides us with the capability to upgrade the underlying instances seamlessly using rolling updates, undo changes, and pause and resume changes as required.

## Creating Deployment

We create a deployment definition file similar to replica set definition file

**deployment-definition.yml**  
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  lables:
    app: myapp
    type: front-end
spec:
  template:
    metadata:
      name: myapp-pod
      lables:
        app: myapp
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx
  replicas: 3
  selector:
    matchLabels: 
      type: front-end
```

- Then run **kubectl create -f deployment-definition.yml**, **kubectl get deployments**, **kubectl get replicaset**, **kubectl get pods**, **kubectl get all** (we can see all created objects)
- **kubectl create -f deployment deployment-definition.yml --record**, it will also create the deployment but it will add the record to 'change CAUSE' when we run 'rollout history' command.
- **kubectl create deployment httpd-frontend --image=httpd:2.4-alpine --replicas=3** : create a deployment with the name "httpd-frontend" using image "httpd:2.4-alpine" and the number of replicas as 3. After running create command chech whether the deployment is created and check for the ready state.
- **kubectl apply -f deployment-definition.yml**, updates the changes made by us to deployment file.
- **kubectl delete deployment myapp**, deleted the deployment named 'myapp'

## Types of Deployment Strategies
We could see the differences between these 2 strategies using **kubectl describe deployment myapp**, the difference would mainly be in scaling.

1. **Recreate**: If we have 5 instances of our application deployed and if we want to upgrade them to new version,  first we need to destroy the previos instances and then deploy the new instances, here we will face down time. This not the default deployment strategy.

2. **Rolling Update**: Here we don't destroy all the instances at once, instead we take down the older version and bring up a newer version one by one. This is default deployment strategy.
- We can update the deployment (updating api version, labels, replicas, images etc.) by changing the 'deployment-definition.yaml' file and then run **kubectl apply -f deployment-definition.yaml**, then a new rollout is triggered and a new revision of the deployment is created.
_ Another way is to run **kubectl set image deployment/myapp \nginx=nginx:1.9.1**, this will result in the deployment definition file having a different configuration.

## Rollout
- When we first create a deployment it triggers a rollout(process of deploying the containers in back end), which is recorded as a new deployment revision.
- when the application or container version is updated to a new one, a new rollout is triggered and a new deployment revision is created.
- This helps us keep track of the changes made to our deployment, and enables us to roll back to a previous version of deployment if necessary.
- **kubectl rollout status deploment/myapp**, shows status of our rollout, here it deploys one pod at a time.
- **kubectl rollout history deployment/myapp**, shows revisions and history of our deployment.
- **kubectl rollout undo deployment myapp**, if something went wrong while upgrading old to new version, then we can use this command. where it destroys pods in new replica set and bring the older ones up in old replica set, and our application will be back to its older format. To see the difference of before and after rollback we can run **kubectl get replicasets**