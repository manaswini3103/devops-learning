# Secrets Management

This is the practice of securely storing, accessing, rotating, and auditing sensitive information without hardcoding them in source code or configuration files.

It is a core DevSecOps practice and critical for cloud-native, CI/CD, and containerized environments.

## Secrets include:

- Database usernames & passwords
- API keys and tokens
- Cloud credentials
- OAuth tokens
- TLS/SSL certificates
- Encryption keys

Bad practice: storing secrets in code, Git repos, Dockerfiles, or plain config files  
Best practice: store secrets in a centralized secrets manager

## Why Secrets Management Matters

- Prevents credential leaks (a leading cause of breaches)
- Enables least privilege access
- Supports automatic rotation
- Improves auditability & compliance
- Enables secure CI/CD and cloud deployments
- Reduces blast radius if a secret is compromised

## How Secrets Management Works (High Level)

- Secrets are stored encrypted at rest
- Applications authenticate to the secrets manager (IAM, Managed Identity, tokens)
- Secrets are fetched at runtime
- Access is logged and audited
- Secrets can be rotated automatically  
secrets like passwords, API keys, or credentials are changed on a regular schedule without manual human intervention, and all systems that use those secrets are updated automatically.

## Tools

### HashiCorp Vault  
Vault is a powerful, cloud-agnostic secrets management platform.

**Key Features**
- Centralized secrets storage
- Dynamic secrets (short-lived credentials)
- Strong encryption
- Fine-grained access control (policies)
- Supports multiple auth methods (JWT, Kubernetes, LDAP)
- Works across clouds & on-prem

### Azure Key Vault  
Azure Key Vault is Microsoft Azure’s native secrets management service.
- Stores: Secrets (passwords, API keys), Keys (encryption keys) and Certificates

**Key Features**

- Integrated with Azure AD (Entra ID)
- Managed identities for apps (no hardcoded creds)
- RBAC & access policies
- Automatic key rotation
- Built-in logging via Azure Monitor

### AWS Secrets Manager  
AWS Secrets Manager is AWS’s fully managed secrets service.

**Key Features**

- Automatic secret rotation (Lambda-based)
- Deep IAM integration
- Encryption via AWS KMS
- Native AWS service integrations
- High availability & scalability

### Differences

| Feature                | Vault     | Azure Key Vault | AWS Secrets Manager |
|------------------------|:---------:|:---------------:|:-------------------:|
| Cloud-agnostic         | yes       | Azure only      | AWS only            |
| Dynamic secrets        | yes       | no              | Limited             |
| Managed service        | Optional  | yes             | yes                 |
| Kubernetes integration | Excellent | Good            | Good                |
| Automatic rotation     | yes       | Limited         | yes                 |
| IAM integration        | Multiple  | Azure AD        | AWS IAM             |