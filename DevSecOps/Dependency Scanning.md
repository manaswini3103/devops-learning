# Dependency scanning

- It is a security practice in DevOps that detects vulnerabilities (any weakness/flaws in an application or system that could be used to compromise its security) in the open-source libraries, packages, containers, and dependencies your application uses. One of the most popular tools for this is Trivy.
- Because modern applications rely heavily on third-party components, dependency scanning is essential for preventing supply-chain attacks and identifying known vulnerabilities (CVEs) early.

## What Dependency scanning Does?

- Analyzes your application’s packages (npm, pip, Maven, Go modules, etc.)
- Checks your container images (Docker images)
- Looks into Infrastructure as Code (IaC) files
- Compares detected components against vulnerability databases (like NVD)


**It identifies**

- CVEs (known security vulnerabilities)
- Outdated or vulnerable libraries
- Malicious or unsafe open-source packages
- Misconfigured dependencies
- Dependency scanning is a core part of shift-left security and DevSecOps.

# Trivy

Trivy (by Aqua Security) is an open-source, all-in-one security scanner widely used in DevOps pipelines.

Trivy can scan:

- Source code dependencies (SCA)
- Container images
- Dockerfiles
- Kubernetes manifests
- Terraform/CloudFormation (IaC)
- Git repos
- SBOMs (Software Bill of Materials)

## How Trivy Works (Simplified)

1. Scan the target  
Example: a Docker image, folder, or repo.
2. Identify components  
Trivy extracts package versions and metadata.
3. Match against vulnerability databases  
Uses:  
- NVD
- Vendor advisories
- GitHub Security Advisories
4. Generate a report  
Includes:  
- CVE number
- severity (Critical/High/Medium/Low)
- fixed version
- affected component

## Why Dependency Scanning (Trivy) Matters in DevOps

1. Protects against supply-chain attacks  
Many major breaches come from vulnerable dependencies.

2. Ensures secure images and containers  
Trivy scans OS packages, library versions, and base images.

3. Early detection (shift-left)  
Vulnerabilities are caught before deployment, saving time and cost.

4. Complements SAST and DAST  
SAST → finds coding issues  
DAST → runtime issues  
SCA (Trivy) → dependency and supply chain issues  

Together they create full-stack application security.

5. Helps with compliance  
Supports standards like:  
- OWASP Top 10
- SOC 2
- PCI DSS
- ISO 27001

## Example

```bash
trivy image my-app:latest # scans a docker image
trivy fs . # Scan source code dependencies
trivy config . # Scan Kubernetes YAML or Terraform
```