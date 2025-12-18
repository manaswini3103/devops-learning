# Blue-green deployment

Blue-green deployment is an application release strategy that minimizes downtime and risk by running two identical production environments in parallel: a "blue" environment with the current live version and a "green" environment with the new version. User traffic is instantly switched from blue to green once the new version has been fully tested and validated.

## Concept

The core concept of blue-green deployment is to have a complete, isolated staging environment that is an exact replica of the production environment.

1. **Blue Environment**: This is the current, live production environment that serves all user traffic. It is a stable, known-working version of the application.
2. **Green Environment**: This is the new staging environment where the updated application code is deployed and tested, isolated from live users.
3. **Zero-Downtime**: The primary benefit is the ability to switch between environments instantly using a load balancer (A load balancer acts like a traffic controller that sends user requests to the healthiest and least busy server.) or router, eliminating the need for a maintenance window and ensuring a seamless user experience.
4. **Instant Rollback**: If issues arise in the green environment after it goes live, traffic can be instantly reverted to the stable blue environment, minimizing the impact of potential problems.
5. **Testing Parity**: Testing is performed in a production-identical environment, which helps catch configuration issues or edge cases that might not appear in a non-production testing environment. 

## Flow

The blue-green deployment process typically follows these steps:

1. **Set Up Environments**: Two identical production environments, blue and green, are provisioned. A load balancer or router is configured to direct all live traffic to the blue (current) environment.
2. **Deploy to Green**: The new version of the application is deployed to the idle green environment.
3. **Test and Validate Green**: The operations team thoroughly tests the new application in the green environment (e.g., security scans, performance checks, smoke tests) without affecting live users.
4. **Switch Traffic**: Once the green environment is validated and approved, the load balancer is updated to instantly route all incoming production traffic to the green environment. The green environment is now the new live production system.
5. **Monitor**: The newly live green environment is closely monitored for any issues or anomalies in a live setting.
6. **Rollback** (if needed): If any critical issues are detected, traffic is immediately switched back to the blue environment, which is still running the previous, stable version.
7. **Decommission or Repurpose Blue**: If the green environment proves stable, the old blue environment can be decommissioned to save costs, or kept on standby to become the "green" environment for the next update cycle.


## Continuous Delivery vs Continuous Deployment

| Aspect                  | Continuous Delivery            | Continuous Deployment                  |
|-------------------------|--------------------------------|----------------------------------------|
| Deployment to production | Manual approval                | Automatic                              |
| Human intervention      | Yes                            | No                                     |
| Release frequency       | Frequent but controlled        | Very frequent (multiple times per day) |
| Risk level              | Lower                          | Higher (managed by automation)         |
| Test automation         | Required                       | Absolutely critical                    |
| Common in               | Enterprises, regulated domains | Tech & cloud-native companies          |
