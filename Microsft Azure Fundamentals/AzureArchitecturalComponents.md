# Core Azure Architectural Components
## Regions
- Regions are areas of the world where Azure has a set of data centers (minimum 3 in a set), not necessarily countries. Usually, each region is connected to another region to make a “region pair” which has highest speed connections and special treatment during Azure updates.
- We can go to this website and see Microsoft data centers and regions https://datacenters.microsoft.com/globe/explore
- Example: Canada has 2 regions – Canada central and Canada east, data stores in these regions never leaves Canada and anyone can use these regions.
- When we create a resource in Azure, we have choice of where to deploy it
- Azure has 60+ regions, but most of them are not available to everyone, like we can’t deploy a VM in all the regions, some regions have a condition that to use the services, we must be the resident of that region.

## Sovereign Azure
They are connected to country or a government but not to Azure public cloud; it requires approval to join/create a subscription. Adhere to different compliance standards.

## Availability Zones
- These are sets of data centers that are physically separate locations within each Azure region. They have their independent power, cooling, connections to internet, they are not reliant on each other for anything.
- Not every region and service supports Availability Zones
- Services like Zonal (we choose main zone to deploy our service, and deploy duplicate of same service to another zone to achieve resilience ex: VMs), Zone-Redundant (automatically deploys across multiple zones, exL Azure SQL Database) and always available services (Microsoft runs these globally, also called as “Non-regional Services”, ex: Azure portal, Azure Front Door) supports Availability Zones.
- Some services give us choice between Zonal and Zone-redundant.



## Resources
- A generic word that represents any Azure service that you have access to, such as a specific virtual machine, a storage account, or some type of database.
- We can create a resource in many ways: Azure portal, CLI, PowerShell, ARM templates etc.
- Each resource has a name created by us, sometimes it has to be unique or unique in resource group or sometime no need to be unique.
- If we deploy resources we need to indicate the region where they are to be created.
- **All Resources**: A brand new subscription is created with no resources, a resource is associated with one and only one subscription, to which its cost is billed.
## Resource Group
- A logical grouping of resources, it is associated with a region, which can be different from than the resources it contains.
- All services in a resource group should have a similar lifecycle- deploy together, delete together.
- All resources must belong to one resource group, we can assign permissions at resource group level. There is no security boundary offered by a resource group for communications.
## Subscriptions
- The billing unit within Azure, subscriptions are associated with a payment method like a credit card (pay as you go). Every resource must exist inside one subscription.
- Administrative boundary for governance, compliance and access control.
- A single user can have access to multiple subscriptions and different roles through RBAC. If we are not in subscription, we can’t see its resources.
- It’s possible to operate an entire organization on a single subscription.
- Some companies choose to have multiple subscriptions to separate out business units within an organization (Sales, IT, Finance) or separate by geography (North America, Asia).
- Subscription Plans
   - Free Plan - $200 credits first 30 days
   - Pay as you Go – billed to credit card
   - Enterprise Agreement – EA
   - Free credits – MSDN, Startup plans
## Management Groups
- Group subscriptions into a hierarchy and manage them on a scale.
- Apply policies, RBAC, governance settings, once at the top level – inheritance.
- Enforce consistent standards across departments.
- Organize large Azure Environments into clean, predictable structure to simply compliance.
