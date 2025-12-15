# Security in the SDLC

- Security in the SDLC (Software Development Life Cycle) refers to embedding security practices, tools, and thinking into every phase of software development rather than treating security as a final step (during testing or just before release).
- The most important idea here is “shifting left” - moving security earlier (to the left side) of the development timeline.
- Instead of discovering security problems after the product is built, you prevent them while it’s being built

## Why Shift Security Left?

1. Fix issues earlier, faster, and cheaper
- A vulnerability found during coding costs 10x less than one found in production.

2. Reduce delays and release bottlenecks
- Early detection avoids last-minute security blocks before deployment.

3. Prevent major vulnerabilities  
You catch:
- insecure design decisions
- poor coding habits
- risky open-source dependencies
- misconfigurations in IaC or cloud setups

4. Enable continuous delivery  
Security automation (SAST, SCA, IaC scanning) fits into CI/CD pipelines.

5. Improves product quality  
Security is built in, not bolted on.

## How Security Fits into Each SDLC Phase (Shift-Left Approach)

1. Planning and Requirements Phase
- Goal is to identify security needs early
- Define security requirements (confidentiality: preventing unauthorized access, integrity: preventing unauthorized modification, availability: systems are available when needed).
- Identify sensitive information (passwords, personal data).
- Perform Risk assesment and Threat modeling (predict how attackers could exploit the system).

2. Design Phase
- Goal is to build a secure architecture (designing Role-Based access control)
- Secure architecture review.
- plan authentication and encryption mechanisms.
- Apply design principles: least privilege, zero trust, defense in depth.

3. Development Phase
- Golas is to follow Secure coding practices and coding standards.
- Avoiding common vulnerability (weakness or flaw in a system) like SQL Injection, XSS, buffer overflow.
- Static Application Security Testing (SAST).

4. Build & Integration
- Dependency scanning / SCA (Software Composition Analysis).
- Automated secrets detection.
- Secure infrastructure-as-code (IaC) checks.

5. Testing Phase
- Dynamic testing (DAST).
- perform security testing (Penetration testing, vulnerability scannning).
- API and container security scans.
- Testing whether attackers can bypass login.

6. Deployment
- Securing production environment and configuration of infrastructure(servers and databases).
- Container image scanning.
- Secrets management.
- Disabling(turning-off) defualt passwords and open ports.

7. Operations & Maintenance
- Continuous monitoring, logging, SIEM.
- Apply security updates and automating patches.
- Responding to incidents and new threats.
- updating software when a vulnerability is discovered.

## Common Shift-Left Security Tools

- SAST: SonarQube, Checkmarx, GitHub CodeQL
- SCA: Snyk, OWASP Dependency-Check
- Secrets Scanning: GitLeaks, TruffleHog
- IaC Scanning: Checkov, Terraform Cloud, Prisma Cloud
- DAST: OWASP ZAP, Burp Suite