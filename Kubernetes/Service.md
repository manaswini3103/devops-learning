# Service

- Kubernetes services enable communication between various components within and outside of the application and helps us connect applications together with other applications or users.
- For example, our application has groups of pods, such as front end, back end, and external data source. It is services that enable connectivity between these groups of pods, front end application to be made available to end users. And helps communication between backend and frontend pods and helps in establishing connectivity to an external data source.


## External Communication.
- For example, we deployed a pod having a web application running on it. And how do we as an external user access the web page?
- The Kubernetes node has an IP 192.168.1.2. Our laptop IP is 192.168.1.1, and pod has an IP 10.244.0.2. We can't ping or access the pod at address 244.0.2 as it's in a separate network.
- So what are the options to see the web page? If we were to SSH into the Kubernetes node at 192.168.1.2, from the node, we would be able to access the pods web page by doing a curl (Curl http://10.244.0.2 : inside the kub node).
- If we want to access web server from our laptop, without having to SSH into the node, and simply by accessing the IP of the Kubernetes node.
- So we need something in the middle to help us map requests to the node from our laptop, through the node to the pod running the web container. This is where the Kubernetes service comes into play.
- The Kubernetes service is an object just like pods, replica sets, or deployments that we worked with before.


## Types of Service
The service is like a virtual server inside the node which is inside the cluster. It has its own IP address, and that IP address is called the cluster IP of the service.

1. **Node Port**
- One of its use cases is to listen to a port on the node, and forward requests on that port to a port on the pod running the web application.
- This type of service is known as a node port service, because the service can help us by mapping a port on the node to a port on the pod.
- There are three ports involved.
  - The port on the pod where the actual web server is running is 80, and is referred as 'target port' because that is where the service forwards the request to.
  - The second port is the port on the service itself and referred as 'port'.
  - Finally we have port on the node itself which we use to access the web server externally known as the 'node port'. And it is set to 30008. node ports will be in range from 30,000 to 32,767.
- We will use a definition file to create a service. spec is the most crucial part of the file as this is where we will be defining the actual services.
- spec section in definition file is the only part that differs between different objects in a service.
- The type refers to the type of service we are creating like cluster IP, node port or load balancer.
This is where we input information regarding what we discussed on the left side of the screen.
- Remember that out of these ports the only mandatory field is port. If you don't provide a target port, it is assumed to be the same as port. And if you don't provide a node port, a free port in the valid range between 30,000 and 32,767 is automatically allocated.
- Also note that ports is an array, so note the dash under the ports section that indicates the first element in the array.
- We mapped target port, but we didn't mention the target port on which pod. There could be hundreds of other pods with web services running on port 80. So we will use labels and selectors to link these together.
- We know that the pod was created with a label, refer to pod definition file used to create the pod. So we need to bring that label into the service definition file.
- We can now use this port to access the web service using Curl or a web browser.

service-definition.yml
```YAML
apiVesrion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: NodePort
  ports:
    - targetPort: 80
      port: 80
      nodeport: 30008
  selector:
    app: myapp
    type: front-end
```
-  **kubectl create -f service-definition.yml**, **kubectl get services**, **curl http://192.168.1.2:30008** : IP and port of the node
- **minikube service myapp-service --url**: we'll get the IP address, we need to give that in a web browser and should be able to access that service.
- This a service mapped to a single pod. If we have multiple similar pods running our web application. They all will have same labels, which is used as a selector during the creation of the service.
- So when service is created, it looks for a matching pod with the label and finds three of them. Then it automatically selects all three pods as endpoints to forward the external requests coming from the user.
- Thus, the service acts as a built in load balancer to distribute load across different pods.
- When web application on pods are distributed across multiple nodes in the cluster. And when we create a service, Kubernetes automatically spans across all nodes in the cluster and maps the target port to the same node port on all the nodes in the cluster. This way, you can access your application using the IP of any node in the cluster and using the same port number, which in this case is 30,008.
  - curl http://192.168.1.2:30008
  - curl http://192.168.1.3:30008
  - curl http://192.168.1.4:30008
- To summarize, in any case, whether it be a single pod on a single node, multiple pods on a single node, or multiple pods on multiple nodes, the service is created exactly the same without you having to do any additional steps during the service creation.
- When pods are removed or added, the service is automatically updated, making it highly flexible and adaptive.

2. **Cluster IP**
- In this case the service creates a virtual IP inside the cluster to enable communication between different services, such as a set of front end servers to a set of back end backend servers.
- A full stack web application typically has different kinds of pods hosting different parts of an application like front end, backend, database (MySQL), Redis.
- The web front end server needs to communicate to the back end servers, and the back end servers need to communicate to the database as well as the Redis services, etc..
- So what is the right way to establish connectivity between these services or tiers of my application?  
The pods have an IP assigned to them, but we can't rely on them for internal communication between the application. As these IPS are not static and these pods can go down any time, and new pods are created all the time.
- A Kubernetes service can help us group the pods together, and provide a single interface to access the pods in a group. For example, a service created for backend pods will help group all the backend pods together and provide a single interface for other pods to access this service.
- The requests are forwarded to one of the pods under the service randomly.
- Similarly, create additional services for Redis and allow backend pods to access Redis systems through service.
- Each service gets an IP and name assigned to it inside the cluster, and that is the name that should be used by other pods to access the service. This type of service is known as **cluster IP** and it is a **defualt** service.
- The 'target port' is the port where the backend is exposed which is 80, and the 'port' is where the service is exposed, which is 80 as well.

service-definition.yml
```YAML
apiVesrion: v1
kind: Service
metadata:
  name: backend
spec:
  type: ClusterIP
  ports:
    - targetPort: 80
      port: 80
  selector:
    app: myapp
    type: back-end
```
-  **kubectl create -f service-definition.yml**, **kubectl get services**, **curl http://192.168.1.2:30008** : IP and port of the node
- a defualat service ClusterIP will be created at launch
- to know thw target port for a service give **kubectl describe service service-name** and look for the field targetPort.
- Endpoints are the parts that the service has identified that is going to direct traffic to based on the selector specified on the service and the labels on the parts. 

3. **Load Balancer**
- It provisions a load balancer for our application in supported cloud providers. A good example of that would be to distribute load across the different web servers in your front end tier.
- So let's focus to the front end applications which are the voting app and the result app.
- We know that these ports are hosted on the worker nodes in a cluster. So let's say we have a four node cluster.
- And to make the applications accessible to external users we create the services of type node port.
- But what URL would you give our end users to access the applications?  
You could access any of these two applications using IP of any of the nodes and the port with the services exposed on. Note that even if your pods are only hosted on two of the nodes, they will still be accessible on the IPS of all the nodes in the cluster.
- So we would share these URLs to your users to access the application. But that's not what the end users want.
- They need a single URL like voting app.com. To achieve this we create a new VM for load balancer purpose and install and configure a suitable load balancer on it like HAProxy Or nginx etc. Then configure the load balancer to route traffic to the underlying nodes.
- Now setting all of that external load balancing and then maintaining and managing that can be a tedious task.
- Kubernetes has support for integrating with the native load balancers of certain cloud providers, and configuring and configuring that for us.
- So all we need to do is set the service type for the front end services to load balancer instead of Nodeport. It only works with supported cloud platforms like GCP, AWS and Azure.
- So if we set the type of service to load balancer in an unsupported environment like VirtualBox or any other environments, then it would have the same effect as setting it to Nodeport where services are exposed on a high end port on the nodes there. It just won't do any kind of, uh, external load balancer configuration.
