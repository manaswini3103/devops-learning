# Recreate deployment

- The Recreate deployment strategy in DevOps is a straightforward approach where the old version of an application is entirely shut down before the new version is deployed.
- This results in a period of downtime, but ensures simplicity, predictability, and that only one version of the application runs at any given time.


## How the Recreate Strategy Works

The process is a simple two-stage operation:

1. **Terminate existing pods**: All running instances of the current application version are stopped.

2. **Create new pods**: Once all old instances are fully terminated, the new pods (containers) with the updated application version are started.
The application is unavailable to users during the time between the old version shutting down and the new version becoming ready to accept traffic.


## Key Characteristics

- Downtime: Involves complete application downtime during deployment.
- Simplicity: Easy to understand and implement with minimal configuration.
- Resource Efficiency: Only one version runs at a time, so it doesn't require double the infrastructure resources, unlike a blue-green strategy.
- Version Management: Guarantees no overlap between the old and new versions, avoiding complex backward compatibility issues.
- Risk: Higher risk for critical production systems, as a failed deployment means the entire application remains down until a fix or rollback is implemented.


## Use Cases in DevOps

Due to the downtime involved, the recreate strategy is typically not recommended for high-availability production environments. It is best suited for:

- Development and Staging Environments: Ideal for testing and QA where a brief outage is acceptable.
- Scheduled Maintenance: Can be used for production deployments if a specific maintenance window has been planned during off-peak hours.
- Batch Processing and Background Jobs: Suitable for tasks that can be paused and restarted without impacting real-time user experience.
- Database Schema Migrations: Useful when a breaking change in a database schema requires that only the new application version can run, ensuring no conflict between simultaneous versions.