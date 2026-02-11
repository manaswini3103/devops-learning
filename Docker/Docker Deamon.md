# Docker Deamon

- The Docker daemon (dockerd) is engine that actually does the Docker work and manages background services like: builds images, runs containers, manages networks & volumes and talks to the OS kernel.
- When we use 'run this container', Deamon finds the image, sets up isolation, starts the container
- The Deamon runs continously, to check it use this command `systemctl status docker` and to start it `sudo systemctl start docker`.
- Deamon Lives in:
  - Binary: /usr/bin/dockerd
  - Config: /etc/docker/daemon.json
  - Socket: /var/run/docker.sock

## Who talks to whom?
we never talk to the kernel directly — the daemon does.  
You (docker command) --> Docker CLI --> Docker daemon (dockerd) --> Linux kernel

## CLI VS Deamon

| Docker CLI       | Docker deamon      |
| ---------------- | ------------------ |
| `docker` command | `dockerd` service  |
| Takes user input | Does the real work |
| Client           | Server             |
| Can run remotely | Runs on host       |

# Docker Architecture

Docker follows a client–server architecture. You give commands → Docker processes them → containers run

1. Docker Client
- The docker command you type in the terminal, Example: 'docker run nginx', it sends requests to Docker, Does not run containers itself.

2. Docker Daemon (dockerd)
- Background service running on the system and main engine of Docker
- What it does: Builds images and Runs containers. If the daemon stops → Docker stops.
- Manages: Networks, Volumes, Storage, Security

3. Docker REST API
- Client and daemon communicate via REST API, which allows remote Docker management
- Example: Docker CLI on your laptop and Docker daemon on a remote server

4. Docker Images
- Read-only templates created from a Dockerfile, which Contain: Application code, Required libraries, Runtime

5. Docker Containers
- Running instances of images which are lightweight and isolated, Example: 'docker run nginx'. One image → many containers.

6. Docker Registry
- Storage for Docker images, Examples: Docker Hub (default), AWS ECR, Azure ACR, Private registry
- Used when images are not available locally.

7. Under the hood (Linux kernel)  
Docker daemon manages all of this for you.  
| Kernel Feature | Purpose          |
| -------------- | ---------------- |
| Namespaces     | Isolation        |
| cgroups        | Resource control |
| UnionFS        | Image layers     |

## Example flow (step-by-step)
- Command: docker run nginx
- What happens:
  - Client sends request
  - Daemon checks local images
  - Pulls image if needed
  - Creates container
  - Starts container process
  - Output returned to client

