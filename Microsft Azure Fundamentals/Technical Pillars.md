# Technical Pillars of Azure
- Computing Services
- Networking Services
- Storage Services
- Database Services


# Computing Services (Executing code in cloud)
Compute Types in Azure: VM, VM Scale Sets (VMSS), App services (Web apps), Azure Container Instances (ACI), Azure Container Apps, Azure Kubernetes Service (AKS), Azure Virtual Desktop.

## Availability Sets
- If we have multiple VMs that have an identical functionality, we want to signify to Azure that they should be separated from each other in a certain way because of Fault Isolation.
- Fault Isolation
  - separate fault domain (power/network outage – if power supply goes to multiple VMs on same rack, because of power outage everything goes down. So, we want them to be separate) and update domain (planned outages – rolling out new version of their platforms, but not for all the servers at once))
  - Separate power sources and network switches
  - updated one at a time, not all together

## Proximity Group
-	If we have multiple VMs that have an identical function


1.	Virtual Machines
- This is the closest analogue to a “server” in cloud computing, but it’s “Virtual”.
- This is a single physical machine that has been subdivided into slices, and you get to rent a single slice of it, and we can get full control over it, as if it was our machine. 
- Take an existing machine from our environment into cloud – a copy. Windows or Linux Oss – several of each, it is an IaaS.
- In Azure we have over 700 VMs to choose from
- In AWS, a VM is called Elastic Compute Cloud (EC2).
- **Standalone Server Analogy**: Think of it as single-detached house, we can do whatever we want with it, it’s difficult to do anything that affects our neighbors (soundproof walls). We don’t share any resources with our neighbors except garbage, sewer, water, electricity.
- **Virtualization Analogy**: Think of a host as an apartment building on the same land and a VM is one of the apartments in that building, where we use common services like garbage, sewer, water, electricity and other services like shared gym, heating/cooling, landscaping. It’s cheaper to rent an apartment than a house. It’s like a house can’t find much difference.

2.	VM Scale Sets
- **Scaling Azure VM**: We can increase size of VM easily, turning a 4 vCPU VM into an 8 vCPU VM in minutes (scale up) (can go to 64 vCPUs or higher). Or we can add more VMs and have them work together to handle the work (scale out).
- VM Scale Sets are a group of VMs that can grow and shrink in quantity based on a predefined rule, usually based on monitoring demand like if CPU utilization is high and server can’t handle the traffic, we can add additional server.
- It can be based on time (schedule) or many other factors.
- If we have two or more VMs running the exact same code, with help of “load balancer” we can direct traffic from one machine to other.
- Autoscaling: adding or removing machines based on demand
- Can handle up to 100 VMs in single scale set, can be configured to increase that to 1000 VMs. If we need more, we can create more scale sets.
