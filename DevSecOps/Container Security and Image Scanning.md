# Container security and image scanning

These are essential practices for ensuring that containerized applications (like those running in Docker or Kubernetes) are safe, trustworthy, and free from vulnerabilities before they are deployed.

These practices help prevent supply-chain attacks, insecure container configurations, and vulnerable base images.

## What Is Container Security?

Container security is the practice of protecting the entire container lifecycle—from building images, storing them, deploying containers, and running them in production.

It includes securing:

- container images
- container runtime
- container registries
- Kubernetes clusters
- container orchestration processes
- CI/CD pipelines

### Key Areas of Container Security

1. Image Security  
Ensuring your container image does not contain:  
- known vulnerabilities (CVEs)
- outdated OS packages
- insecure dependencies
- hardcoded secrets
- unnecessary tools (like ssh, curl)

2. Runtime Security  
Monitoring containers while they are running:
- detecting malicious processes
- blocking privilege escalation
- detecting abnormal network activity

3. Configuration Security  
- Preventing insecure container settings:
- running as non-root
- using read-only filesystem
- proper resource limits
- secure network policies

## What Is Image Scanning?

Image scanning is the process of checking a container image for vulnerabilities and misconfigurations before deployment.

### A scanner analyzes:
- OS packages (APK, APT, RPM)
- libraries and dependencies
- environment variables
- secrets embedded in the image
- Dockerfile configuration issues

Image scanning catches vulnerabilities early (shift-left) in CI/CD.

### How Image Scanning Works

The scanner inspects your image layers.

- It extracts software versions, libraries, and metadata.
- It checks for CVEs using vulnerability databases.
- It identifies misconfigurations (e.g., running as root).
- It generates a security report (JSON, HTML, CLI output).

### Tools for Container Image Scanning

1. Trivy (most widely used, open source)  
Scans:
- images
- file systems
- dependencies
- IaC
- SBOM

2. Anchore/Grype  
Lightweight vulnerability scanner.

3. Clair  
Registry-based scanning.

4. Aqua Security / Prisma Cloud / Qualys  
Enterprise-grade solutions.

5. Docker Hub built-in scanning  
(uses Snyk in many cases)


### Image Scanning in CI/CD (DevOps Workflow)

- Developer commits code
- CI builds a Docker image
- Scanner (e.g., Trivy) runs automatically
- If vulnerabilities exceed policy thresholds (e.g., Critical/High), the pipeline fails
- Only secure images get pushed to registry
- Kubernetes deploys trusted images only
- Example GitHub Actions step:
  ```yaml
  name: Scan container image with Trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: my-app:latest
    exit-code: 1
    severity: CRITICAL,HIGH
  ```
- This fails the pipeline if high/critical issues are found.

##  Why Container Security and Image Scanning Matter

1. Protects against supply-chain attacks  
Most breaches today come through compromised dependencies or images.

2. Prevents deploying vulnerable containers  
Keeps production environments safe.

3. Ensures compliance  
Helps meet requirements for:  
- PCI DSS
- ISO 27001
- SOC 2
- NIST

4. Eliminates unnecessary attack surface  
By scanning base images and removing unnecessary software.

5. Helps enforce DevSecOps best practices  
Security becomes part of the pipeline, not an afterthought.

