# Cloud Service Types
There are three types of services

1.	Infrastructure As a Service
2.	Software As a Service
3.	Platform As a Service
- “As a Service” means we can rent service for a short time, no commitment, pay for what you use, cloud provider takes care of buying, developing and maintaining it.

1. Infrastructure As a Service
- These are essential services: Computing, Storage, Networking.
- Generally, have “real world” equivalents in our own data center.
- Cloud replacements of real-world things
- IaaS Computing: one example is Azure VMs; Pay by the second; Many choices in CPU speeds, RAM, optimizations.
- IaaS Storage: Azure Storage; 5 PB of storage capacity; can handle blobs, files, queues and tables; configured as a data lake.
- Iaas Networking: Virtual Networking, don’t cost anything, there are ingress and egress bandwidth costs.

2. Platform as a Service (PaaS)
- Cloud service providers have an opportunity to provide more than “basic” infrastructure.
- It includes a service layer on top of IaaS
- Middleware, development tools, database servers, and more
- PaaS Computing: example is Azure App Services, we upload our code and configuration to Azure, and it runs our code without worrying about VM underneath. Includes scaling features, CI/CD, containers, staging and development environments, etc.
- PaaS Storage: Manages Storage, Azure SQL Database, no need to worry about VM or hard drive
- PaaS Networking: Azure Front Door, Loads Balancer, Firewall, these perform networking tasks

3.	Software as a Service (SaaS)
- Cloud apps, tools such as Office 365, One Drive, Skype
- The app is ready to be used, and we need to set it up and use it

# Serverless
- We don’t manage the servers; we only handle writing and running the code, we focus on code not on infrastructure.
- No charge when our app or database is idle, no need to prepurchase or reserve resources.
- Example – SQL Database Options
Azure SQL Database has multiple pricing options:
1. DTU-based: Fixed performance levels (S1, S2, etc.)
2. vCore-based: we choose CPU, memory and storage
3. Serverless: Auto-scales CPU and memory based on usage
- Key Features: Azure auto-scales between 0.5 to 80 vCores, charged per vCore-second and storage used. It can pause when idle, cutting costs entirely.
- Example of Azure Functions: first 1 million executions per month are free, after that we pay per execution and it’s time. Azure handles scaling automatically.
- Advantages: No server management, scales automatically, cost efficient for intermittent workloads.
- Disadvantages: Costs may vary month to month, cold starts may cause slight delays