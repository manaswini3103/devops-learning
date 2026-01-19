# Docker

- Docker is a containerization or OS‑level virtualization platform that enables you to create, deploy, and run applications conveniently with the help of containers.
- This is used to package your application and all its dependencies together in the form of containers to make sure that your application works seamlessly in any environment which can be developed or tested or in production.
- Written in the Go programming language.
- we just need Docker to be installed on our systems and build the docker configuration. Then developers could get started with a simple Docker run command, irrespective of what the underlying OS they run.


## Containers

![Docker](../images/vmvsdock.png)

- A Container is a lightweight, standalone/Isolated (can have their own processes/services, network interfaces amd mounts) package that include everything an application needs to run (code, runtime, configuration files, all required libraries, dependencies, settings).
- This ensures the application behaves the same way whether on a developer’s laptop, testing environment, or production server.
- Unlike traditional virtual machines that carry a full OS, containers only pack what is required, making them faster and more efficient.
- Containers have existed for about 10 years now and some of the different types of containers are LXC, LXD, LXCFS etc. Docker utilizes LXC containers.
- setting up  container environments is hard as they are very low level. That is where Docker offers a high level tool with several functionalities making it easy for end users like us.

### container vs Virtual Machines

![Docker](../images/vmvscontainer.jpg)

### Containers and Virtual Machines

![Docker](../images/vmandcontainer.jpg)

- Now when you have large environments with thousands of application containers running on thousands of docker hosts, you will often see containers provisioned on virtual docker hosts.
- We can use the benefits of virtualization to easily provision or decommission docker hosts as required.
- At the same time make use of Docker to easily provision applications and quickly scale them as required.
- In this case we will not be provisioning many VMs as we used to provision VM for each application. Now we may provision a VM for hundreds or thousands of containers.

### Container vs Image

| Feature                | Image                           | Container                   |
| ---------------------- | --------------------------------|--------------------------- |
| State                  | Static                          | Running instances of images |
| Read/Write             | Read-only                       | Read + Write                |
| Purpose                | Template like VM                | Execution                   |
| Exists Without Running | Yes                             | No                          |
| Multiple Instances     | One image - 1 or many containers| Each is separate            |
| Changes Persist        | No                              | Only while container exists |


## Before Docker

- Suppose there are three developers in a team working on a single project.
- Meanwhile, each one of them has a Windows, Linux and MacOS.
- As they are using different environments for creating a single application, they are required to carry on
specific libraries, versions, Specific runtime (Java, Python, Node, etc.), files for their system, Environment variables and system settings.
- On an organizational/larger level deploying applications across different environments was often difficult, dependencies, configs, and OS variations caused “works here but not there” headaches.

## Advantages

Standardizes the runtime environment by bundling everything (app + dependencies) into containers.

- Portability: Build once and runs anywhere in local machine, Windows, macOS, Linux, cloud, on‑prem servers. And there is no need of environment rewrite.
- Consistency: Containers guarantees that an application can run the same way on any environment(Developmet, Stages, Testing, Production), eliminating "it works on my machine" problem.
- Isolation: Docker containers isolate applications from each other and from the host system allowing multiple applications to run securely on a single host without interfering with one another.
- Lightweight: allows applications to share the host OS kernel instead of running a separate guest OS like in traditional virtualization.
- Scalability: Docker makes it easy to scale services up or down as needed. Container orchestration platforms like Kubernetes or Docker Swarm can automatically manage, scale, and orchestrate containers across a cluster of machines
- Efficiency and Resource Optimization: As it shares Host OS kernel, they start up quickly, use fewer resources, and allow more containers to run on the same hardware.
- Simplified Management: Docker provides a simple command-line interface (CLI) and a clear, image-based system for tracking dependencies, manage different versions of an application, and roll back updates if necessary.
- Faster Development Cycles: Docker streamlines the build, test, and deployment process. Developers can quickly set up complex development environments, collaborate easily by sharing container images, and deploy applications rapidly across various environments.
- Easy Setup: New developers can start instantly, Faster onboarding, No complex setup.