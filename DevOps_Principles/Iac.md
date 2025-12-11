# Infrastructure as Code

Infrastructure as Code (IaC) is the practice of managing and provisioning infrastructure (servers, networks, databases, load balancers, etc.) using code, rather than manually configuring hardware or cloud resources.

- Instead of clicking through cloud dashboards (AWS, Azure, GCP), you write code files that describe the infrastructure you want.
- Instead of manually creating a server
    - Traditional way: Click "Create EC2 Instance" on AWS console.
    - IaC way: Write code like
    ```yaml
    resource:
      aws_instance:
        web:
          ami: "ami-12345"
          instance_type: "t2.micro"
    ```

## Why IaC Is Important in DevOps

IaC is a core DevOps practice because it enables:

- **Automation**: Infrastructure is created, updated, and deleted automatically.
- **Consistency**: Same code deploys the same environment every time (no human errors).
- **Speed**: Deploy environments in minutes instead of hours or days.
- **Scalability**: IaC can create 1 or 100 servers with the same script.
- **Version Control**: Infrastructure code can be stored in Git like application code.
- **Reproducibility**: You can recreate entire environments (QA, staging, prod) anytime.

## How IaC Works

1. Write a configuration file: Describe your infrastructure using code (YAML, JSON, HCL, etc.).
2. Submit the code (usually through CI/CD): Commit it to Git → triggers automation.
3. IaC tool reads the file: The tool compares your desired state with the actual state.
4. IaC tool creates or updates infrastructure: It builds or modifies infrastructure to match your code.

This is called desired-state management.

## Core Concepts of IaC

1. Idempotency
- This means running the same script repeatedly always produces the same result, no matter how many times it runs.
- If the infrastructure already matches the desired state, the tool will simply do nothing
- This prevents:
    - Duplicate servers
    - Misconfigurations
    - Drift
- Example: If the script says “1 server,” running it 10 times still keeps 1 server, not 10.

2. Immutable Vs Mutable Infrastructure  

**Mutable Infrastructure**: This is the traditional "pet" model. Servers are provisioned and then updated, patched, and modified in place over their lifetime. This process can lead to configuration drift and makes servers fragile and unique.

**Immutable Infrastructure**: This is the modern "cattle" model favored by IaC.
- once a server or environment is created, it is never modified.
- If you need to change something (update version, fix config, add software), you do NOT update the existing server.
- Instead you'll replace it entirely with a new, updated version (Think of it like replacing rather than repairing).
- After deployment, the infrastructure components are treated as unchangeable (immutable).
- No SSH → No manual changes → No configuration drift.

**How It Works**

- Create a server image (e.g., AMI, Docker image)
- Deploy it to production
- Need changes:
    - Build a new image
    - Deploy the new instances
- Delete the old ones


## Popular IaC Tools

### Infrastructure Provisioning Tools

These tools are primarily used to create, modify, and destroy the foundational infrastructure components like virtual machines, networks, and databases. They are almost always declarative.

1. **Terraform**: A widely-used, open-source tool by HashiCorp. Its key feature is being cloud-agnostic, supporting **AWS**, **Azure**, **GCP**, and many other providers. It uses a declarative language (**HCL**) and excels at managing complex, multi-cloud infrastructure.
2. **AWS Cloud Formation**: The native IaC tool for AWS. It allows you to define AWS resources in **JSON** or **YAML** templates. Its main strength is its deep integration with all AWS services.

### Configuration Management Tools

These tools specialize in configuring the software on existing servers. They install packages, manage configuration files, and ensure services are running.

1. **Ansible**: A very popular open-source tool known for its simplicity and agentless architecture. It uses **YAML playbooks** that are easy to read and operates over SSH. It can be used for both imperative (tasks) and declarative (state) management.
2. **Puppet**: A mature, agent-based tool that uses a declarative, model-driven approach. A central "Puppet Master" server manages the "Puppet Agents" on each machine, enforcing the desired state.
3. **Chef**: A powerful and flexible agent-based tool that uses a Ruby-based DSL (Domain-Specific Language). It's often described as more imperative, giving developers fine-grained control over configuration steps using "recipes" and "cookbooks."
4. **Salt Stack (Salt)**: A high-speed, event-driven automation tool. It can operate in either an agent-based model or an agentless model over SSH and is known for its performance and scalability.

### Container Orchestration Tools

While not strictly traditional IaC, these tools manage the infrastructure and lifecycle of containerized applications in a declarative way.

1. **Kubernetes (K8s)**: The de-facto standard for container orchestration. Kubernetes automates the deployment, scaling, and management of containerized applications. Users define the desired state of the application (e.g., "run 3 replicas of this container and expose it on port 80") using YAML manifests.


## Two Types of IaC

1. **Declarative IaC** (most common)  
You define what you want, and the tool decides how to do it.  
Example: Create 3 servers.  
Tools: Terraform, CloudFormation.

2. **Imperative IaC**  
You define exact steps to achieve something.  
Example: Create server → install packages → configure service → start service.  
Tools: Ansible, scripts.