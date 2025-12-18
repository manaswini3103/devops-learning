# Rolling Updates
- Rolling updates are a core DevOps technique for zero-downtime deployment (ZDD), allowing seamless application upgrades by incrementally replacing old instances with new ones.
- It ensures continuous availability for users by gradually shifting traffic and verifying health at each step, often managed by orchestrators like Kubernetes.
- This minimizes risk, enhances user experience, and integrates well with CI/CD pipelines, preventing the disruptions common in traditional "big bang" updates. 

## How Rolling Updates Work

1. **Gradual Replacement**: Instead of deploying all new instances at once, it updates pods/servers in small batches.  
Users → LB → v1-Instance-1
              v1-Instance-2
              v1-Instance-3  
Where  
Users: End users (browsers, mobile apps, APIs) sending requests to the application.  
LB (Load Balancer): Receives all user requests, Distributes traffic only to healthy, active instances and Automatically excludes instances that are being updated.  
Tv1-Instance-1 & v1-Instance-2 & v1-Instance-3: These are three running application instances
2. **Traffic Shifting**: A load balancer directs traffic away from an old instance (v1-Instance-1), which is then updated (to V2) or restarted or running health checks.  
Users → LB → v1-Instance-2
              v1-Instance-3

3. **Health Checks**: The system waits for the new instance to become healthy and ready to serve requests before proceeding. And then add back to traffic.  
Users → LB → v2-Instance-1
              v1-Instance-2
              v1-Instance-3

4. **Incremental Rollout**: This process repeats, ensuring that enough healthy instances always exist to handle user traffic. Update the next instance and Continue until all instances run v2.  
Users → LB → v2-Instance-1
              v2-Instance-2
              v2-Instance-3

## Key Benefits

- Zero Downtime: Users experience no interruptions during updates.
- Reduced Risk: Small, incremental changes are easier to monitor and roll back if issues arise.
- Better User Experience: Prevents frustration and lost revenue from service unavailability.
- Automation-Friendly: Works seamlessly with CI/CD tools and container orchestrators.

## Tools & Implementation (e.g., Kubernetes)

- Kubernetes Deployments: Natively support rolling updates, automatically managing pod/server creation/deletion and resource allocation.
- Readiness Probes: Essential for Kubernetes to know when a new pod is truly ready to accept traffic.
- Graceful Shutdowns: Allow existing requests on old pods to finish before termination.


## Canary vs Rolling vs Blue-Green

| Strategy     | Risk      | Rollout Speed | User Exposure        |
|--------------|-----------|---------------|----------------------|
| Blue-Green   | Low       | Fast          | All users            |
| Rolling      | Medium    | Medium        | All users gradually  |
| Canary       | Very Low  | Slow          | Subset of users      |
