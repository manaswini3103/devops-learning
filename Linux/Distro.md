# Linux Distributions (Distros)

Linux comes in many versions called *distros*. They all use the same kernel but include different software and interfaces. Since Linux is open source, anyone can modify and share their own versions.

To know what Linux Distribution we have we can read **cat /etc/os-release**


## Popular Linux Distributions

- **Ubuntu**: One of the most popular and versatile distributions, known for its user-friendliness.
- **Debian**: A highly stable, community-developed distribution that is the foundation for many other distros, like Ubuntu.
- **Fedora**: An innovative distribution sponsored by Red Hat, often featuring new technologies.
- **Linux Mint**: A user-friendly distribution based on Ubuntu, popular for desktop use.
- **Arch Linux**: A lightweight and highly customizable distribution that follows a “rolling release” model.
- **CentOS**: A community-supported Linux distribution based on the source code of Red Hat Enterprise Linux (RHEL).
- **openSUSE**: A community-developed distribution from Germany with both stable and rolling release versions.
- **Kali Linux**: A specialized distribution for penetration testing and digital forensics.

# CentOS vs Alpine Comparison

| Feature        | CentOS                | Alpine                        |
|----------------|-----------------------|-------------------------------|
| Purpose        | Enterprise servers    | Lightweight Dockercontainers  |
| Size           | Large                 | Very small                    |
| Package Manager| yum/dnf               | apk                           |
| C Library      | glibc                 | musl                          |
| Init System    | systemd               | OpenRC                        |
| Stability      | Very high             | High but minimal              |
| Best For       | Servers               | Docker images                 |