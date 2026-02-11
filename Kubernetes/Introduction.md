# Kubernetes
- Kubernetes, also known as K8's, was built by Google based on their experience running containers in production.
- It is now an open-source project (supported by all cloud service providers like GCP, Azure, AWS) and is one of the **popular Container Orchestration Technologies that manages and deploys thousands of containers in a cluster**.
- **Container Orchestration**: If our application relies on other containers, and to scale up and down the resources. We need a platform with set of resources, which could orchestrate the connection between containers and automatically scale up
or down based on the load. The process of automatically deploying and managing containers is called Container Orchestration.
- We have Container Orchestration tools like Docker Swarn (from Docker, easy to set up and start, but lacks some advanced features), Kubernetes (from Google, difficult to set up and get started, but has options to customize deployments of complex architectures) and MESOS from Apache.

## Kubernetes Components
When we install Kubernetes on a system, we install the following components an API server, etcd service, a Kubernetes service, a container, runtime controllers and schedulers.
- **API Server**: acts as Front End for Kubernetes, where users/CLI talk to API to interact with Kubernetes Cluster.
- **Etcd**: distributed, reliable key value store, which stores all data used to manage the cluster, like all nodes and masters in a cluster. It is responsible for implementing locks within the cluster to ensure that there are no conflicts between the masters.
- **Scheduler**: responsible for distributing work or containers across multiple nodes. It looks for newly created containers and assigns them to nodes.
- **Controllers**: they are the brain behind orchestration, responsible for noticing and responding when nodes, containers, or endpoints go down, they make decisions to bring up new containers.
- **Container Runtime**: underlying software that runs containers. Example Docker.
- **Kubelet**: agent that runs on each node in the cluster, which is responsible for checking that the containers are running on the nodes as expected.


## Kubernetes Architecture
1. Nodes: A node is a machine, physical or virtual, where containers will be launched by Kubernetes. It was also known as minions in the past.
- What if the node on which your application is running fails? Then our application goes down, so we need to have more than one node.
- A cluster is a set of nodes grouped together. So, if one fails the application would be accessible from other nodes.
- The master is another node with Kubernetes installed in it and is configured as a master, it watches over the nodes in the cluster and is responsible for the actual orchestration of containers on the worker nodes.	


