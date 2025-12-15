# Continuous Monitoring

Monitoring means continuously tracking the health, performance, and behavior of applications and infrastructure in real time.

- We can continuously monitor and can get notified before anything goes wrong with the help of **Prometheus**, we can gather many performance measures, including CPU and memory utilization, network traffic, application response times, page load time, error rates, and others.
- **Grafana** makes it possible to visually represent and keep track of data from time series, such as CPU and memory utilization.

## Goals of Monitoring

- Detect issues early
- Enable fast incident response
- Reduce downtime and performance problems
- Understand system behavior under load
- Improve user experience

## What DevOps Teams Monitor

- Application metrics: response time, error rates, latency
- Infrastructure metrics: CPU, memory, disk, network
- Logs: application logs, system logs, audit logs
- Events: deployment events, failures, scaling events
- User experience: page load time, customer journeys

# Continuous Feedback

Continuous Feedback can increase the performance of the application and reduce bugs in the code making it smooth for end users to use the application.

- Once the application is released into the market the end users will use it, they give us feedback about the performance of the application and any glitches affecting their experience.
- After getting multiple feedback from the end users' the DevOps team will analyze the feedbacks and will reach out to the developer team.
-Developers tries to rectify the mistakes they are performed in that piece of code by this we can reduce the errors or bugs that which we are currently developing and can produce much more effective results for the end users.
- Also we reduce any unnecessary steps to deploy the application.

## Observability (Modern Monitoring)

- Beyond regular monitoring, observability helps teams understand why something is happening, not just what is happening.
- It uses: Metrics, Logs and Traces (track request flow through microservices)

This helps diagnose complex issues in distributed systems like Kubernetes setups.

## Feedback Loops in DevOps

Feedback loops ensure that insights from users, monitoring, testing, and production automatically flow back into development.The faster the feedback, the quicker the improvement.

### How Feedback Loops Work

- Code is deployed
- Monitoring detects performance or errors
- Alerts or dashboards show the issue
- Teams review logs, metrics, and user data
- Insights go back to developers
- Developers fix issues or improve features
- CI/CD deploys changes again

This creates a continuous cycle of improvement.

### Types of Feedback in DevOps

1. Real-time system feedback
- Alerts from monitoring tools
- Automatic notifications (Slack, email, pager)
- Auto-remediation scripts

2. User feedback
- Error reports
- Feature usage analytics
- Customer support tickets

3. Pipeline feedback
- Failed builds
- Failed tests
- Security scan results