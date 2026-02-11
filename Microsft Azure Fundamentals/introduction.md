- The Azure Fundamentals exam tests your foundational level knowledge of cloud services and how those services are provided within Microsoft Azure.
- The cloud is just someone else's computer.
- Microsoft Azure has billions of dollars invested in data centers and fiber optic cables, satellites, and all sorts of infrastructure around the world that you can utilize.
- **cloud computing**: The ability to rent computing on demand is really what sets the cloud apart from other types of hosting or on premises services. Renting computing resources, means Windows and Linux servers are available and unlimited file storage which we'll never be able to fill it.


## Public vs Private vs Hybrid

## Advantages Of Cloud Computing

1. High Availability:
- Ability of a system to remain operational to users during planned (we can have a maintenance window or mention specific time) or unplanned outages.
- planned: OS security patches, Application updates, Hardware replacement, Migrating to a new hosting provider.
- Unplanned: Hardware Failure, Network/internet disruptions, power outages, Natural Disasters like earth quake, Cyber Attacks, Software bugs, poor scaling / architecture design

**Methods to Mitigate Planned Outages**
- Gradual Deployment Strategy, small and frequent deployments, automation of deployments
- testing and monitoring of deployment
- Easy rollback plans

**Methods to Mitigate Planned Outages**
- Every single core component has redundancy
- using Azure's built-in features for availability (Availability Sets, Availability Zones, Cross Region load Balancing / Front Door)
- constant health monitoring / probes, strong security practices
- Automation, load testing
- Be geographically disturbed (avoiding issues related to location)
- Have a disaster Recovery plan, test that recovery plan / fire drills

2. Scalability
The ability of a system to accommodate increasing demand by adding or removing resources as needed. Adding more resources to a system add to cost, reducing resources can reduce cost. 
**why it is needed**
It allows a system to adapt to changing usage patterns and handle increased traffic without requiring changes to application code and or system design
**Does traffic Fluctuate**
- Some businesses have traffic that fluctuates based on time of the day or day of the year
- E-Commerce websites having Black Friday Sale, where the traffic becomes high
- School Registrations are busy in September, tax systems are busy in April  
**Vertical Scaling** 
- Also called as ‘Scaling Up’ and ‘Scaling Down’
- Adding more resources to a single server
- Increasing the amount of memory, by increasing the number of CPUs
- There is a upper limit to it, which means limit to increasing number of CPUs and memory, for Azure 96 vCPUs, 384 GB memory
- If we take single CPU server and increasing it’s capacity, it doesn’t improve availability.  
**Horizontal Scaling**
- Also called as ‘Scaling Out’ and ‘Scaling In’
- Adding more servers to a system, no limits to scaling
- Additional complexities for load balancing and can improve availability.

3. Elasticity
The ability of a system to quickly and easily scale up and down the number of resources that a system uses in response to changing demand.
- Has to involve Automation like system need to detect if it is running out of resources or exceeds a limit for being busy, then it need to add more resources and removes resources when it falls below a limit for being not busy. All these is called as ‘Auto Scaling’ in cloud computing.  
**why it is needed**
- More Efficient and Cost-Effective use of resources.
- Minimizes computing waste – resources paid for and not used
- Self Hosted Systems tend to have a large percentage of ‘over-provisioned’ resources for anticipating future growth. Which end up having maximum capacity than it is needed and more than our affording capacity.

4. Reliability
- The ability of a system to recover from failures.
- Azure has several built-in services that we can use to keep an application running after a failure has occurred. Failures like: Hardware failure, network interruptions, power failures, large-scale regional outage.
- This includes transparency during service issues.
- Reliability is achieved in Azure through: Auto-scaling, Multi-region deployments, Avoid single points of failure, Data backup and replication, health probes and self-healing.

5. Predictability
- The ability to forecast and control the performance and behavior of a system, it includes ability to predict future costs, so we don’t get a crazy bill unexpectedly.
- It gives us the confidence that system will continue to perform at expected level in the future.
- It is achieved through: Autoscaling; load balancing; different instance types, sizes, pricing tiers; cost management tools; API.

6. Security
- Cloud providers are massive targets for hackers, so they spend a lot of time, money and effort on platform security. And go through security audits and compliance certifications.
- Provides to customers which enable and monitor security with their own applications/data.
- Why it is needed: Security is a fundamental challenge in IT; it provides confidence that our cloud provider cannot easily be defeated by hackers.
- How it is achieved: They follow Industry Standard compliance certifications, Microsoft Security Response Center(MSRC), Always-on DDos, Azure Policy, Role bases access control, Entra ID (formerly Azure Active Directory), Always up-to-date platform services, update management (if we are using own IAC), Encryption by default, Dozens of security services.

6. Governance
- How our organization does business
- The process of defining, implementing, and monitoring a framework of policies that guides organizations cloud operations.
- Why it is needed: when company wants it’s policies are followed in cloud, including basic auditing and reporting and enforcement, compliant with industry standards like HIPAA/PCC/GDPR.
- How is it Achieved: Azure Policy & Blueprint, Management groups, Custom roles, Soft delete for storage accounts, Guides and best practices such as Cloud Adaption Framework.

7. Manageability
Management of the Cloud (managing our own applications in cloud)
- Templates, Automation, Scaling, Monitoring and alerts, Self-Healing
Management in the Cloud (managing cloud itself)
- could provide features like Webportal, CLI and scripts, APIs, PoerShell to manage our resources
- Why Is It Needed: Easy to work with our applications in the cloud impacts cost, performance, security and other priorities. Some cloud vendors are easy to work with some are hard.
- How Is It Achieved:
  - Azure Portal, CLI, PowerShell, Cloud Shell, TEST APIs and other programmatic methods.            consolidated monitoring and alaerting system
  - Ability to use ARM templates, Bicep, Terrafrom etc
  - Autoscaling of most types of compute resources.









