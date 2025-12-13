# Secure CI/CD pipelines

- This ensure that code is built, tested, and deployed safely, preventing vulnerabilities, secrets leaks, and malicious code from reaching production.
- They are a core part of DevSecOps, where security is embedded into automation—not added later.


## Why Securing CI/CD Pipelines Matters

- CI/CD pipelines have high privileges (cloud access, deployment rights)
- Compromised pipelines can:
    - inject malicious code
    - leak secrets
    - deploy vulnerable applications
    - Many real-world breaches originated from insecure pipelines

## Key Security Practices in CI/CD Pipelines

1. Source Code Security
- Protect main branches, Require pull requests & reviews.
- Enable signed commits, Scan for secrets before merge.
- Tools: GitHub branch protection, GitLeaks

2. Secrets Management
- Never hardcode secrets in pipelines
- Fetch secrets at runtime from: Vault, AWS Secrets Manager and Azure Key Vault
- Use short-lived credentials

3. Dependency & Supply Chain Security

- Scan open-source dependencies, Validate package integrity and Generate SBOMs.
- Tools: Trivy, Snyk, Dependabot

4. Static Application Security Testing (SAST)
- Scan source code for vulnerabilities early
- Fail the builds on critical issues
- Tools: SonarQube, CodeQL

5. Container & Image Security
- Scan container images before pushing
- Use minimal, trusted base images and Enforce non-root containers
- Tools: Trivy, Grype

6. Infrastructure as Code (IaC) Security
- Scan Terraform, CloudFormation, Kubernetes YAML and prevent insecure configurations
- Tools: Checkov, tfsec, Trivy config

7. Pipeline Access Control
- Apply RBAC to CI/CD systems and Separate build and deploy roles.
- Restrict who can modify pipelines

8. Artifact Integrity & Signing
- Sign build artifacts and images
- Verify signatures before deployment
- Tools: Cosign, Notary

9. Environment Promotion Controls
- Dev → Test → Prod approvals
- Manual approval gates for production
- Policy-as-code enforcement

10.  Monitoring & Audit Logging
- Log all pipeline executions
- Monitor for anomalies
- Track who deployed what and when

## Secure CI/CD Pipeline Flow

- Developer pushes code
- Secrets scan runs
- SAST scan checks code
- Dependencies scanned
- Docker image built
- Image scanned
- Artifact signed
- Manual approval
- Deployment to production
- Runtime monitoring