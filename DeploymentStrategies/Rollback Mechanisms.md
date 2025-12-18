# Rollback Mechanisms

- **Rollback**: It is the process of reverting an application or system to a previous stable version when a deployment causes failures or issues.
- rollback mechanisms (like Blue/Green, Canary, Feature Flags) are safety nets for failed deployments. And they're integral to continuous delivery, enabling teams to deploy confidently by ensuring a reliable, fast escape route when things go wrong, reducing risk and improving system resilience. 
- while best practices emphasize automation, testing, version control, and monitoring to ensure fast, reliable reversion to a stable state, minimizing downtime and data loss through small, frequent changes and robust CI/CD pipelines.


## Common Rollback Mechanisms 

1. Blue/Green Deployments: Run two identical environments (Blue=live, Green=new). Switch traffic to Green upon success; instantly switch back to Blue if issues arise.

2. Canary Releases: Roll out to a small user subset first, monitor, then expand. Revert only the canary group if problems occur.

3. Feature Flags (Toggles): Turn off problematic features instantly in production without redeploying the whole app.

4. Versioned Deployments: Keep multiple versions running, allowing quick switching to a known-good build, common in microservices.

5. Rolling Rollback: Gradually replace new version instances with old ones


## Best Practices

- Automate Everything: Automate rollback steps within CI/CD pipelines to remove manual errors.
- Test Rollbacks: Rehearse rollback procedures in staging like fire drills.
- Version Control & Artifacts: Keep all code, configs, and infrastructure code in Git; maintain accessible, known-good build artifacts.
- Monitor & Alert: Use tools (Prometheus, Grafana) to detect failures (errors, latency, crash loops) early and trigger alerts/rollbacks.
- Keep Changes Small: Smaller, frequent deployments are easier and faster to revert.
- Document & Plan: Create clear rollback plans with failure criteria, escalation paths, and responsible persons before deploying.
- Immutable Infrastructure: Deploy new containers/images/VMs rather than modifying existing ones for consistency. 

