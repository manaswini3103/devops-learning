# Controllers

- The **replication controller** helps us run multiple instances of a single pod in the Kubernetes cluster, so if one fails other pods could serve the application or when numbers of users increase, we deploy additional pods or nodes to balance load. Even if we have single pod this controller can help by automatically bringing up a new pod when the existing one fails.
- The Replication Controller is older technology that is being replaced by **Replica Set**
- How does the replica set know what pods to monitor? This is where we use labels of our pods during creation. We could provide these labels as a filter for replica set under the selector section; we use the Match labels filter and provide the same label that we used while creating the pods.
- If the pods where already created, do we need to still mention the “template” section? Yes, if the pods fail replica set will create new pods by using template section.


## Creation Of Replication Controller

**rc-definition.yml**  
```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: myapp-rc
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
    matchLabels: # The match labels selector simply matches the labels specified under it to the labels on the pods.
      type: front-end
```
- Then run **kubectl create -f rc-definition.yml**, output: replicationcontroller "myapp-rc" created.
- **kubectl get replicationcontroller**, list the created replication controller.
- **kubectl get pods**, we'll see the replica pods created by replication controller

## Creation of Replica Set
**replicaset-definition.yml**  
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: myapp-replicaset
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
```

- Then run **kubectl create -f replicaset-definition.yml**, output: replicationcontroller "myapp-rc" created.
- **kubectl get replicaset**, list the created replication controller.
- **kubectl get pods**, we'll see the replica pods created by replication controller
- **kubectl scale --replicas=6 -f replicaset-definition.yml** or **kubectl scale --replicas=6 replicaset myapp-replicaset**, the number of replicas in the replica set definition file will still be three, even though you scaled your replica set to have six replica
- **kubectl delete replicaset myapp-replicaset**, deletes all underlying pods
- **kubectl replace -f replicaset-definition.yml**, replace or update the replica set.
- **kubectl edit replicaset myapp-replicaset**