# Package Management
Package managers streamline the installation, update and removal of software. Each distribution uses its own package management system. These are software tools designed to automate these tasks and manage dependencies.

- To know what Linux Distribution we have we can read **cat /etc/os-release**.  
output: NAME="Ubuntu"  
VERSION="22.04.3 LTS (Jammy Jellyfish)"  
ID=ubuntu  
ID_LIKE=debian  
- And to know which type of package management our system is using give **which apt dnf yum pacman zypper**  
output: /usr/bin/which: no apt in (/sbin:/bin:/usr/sbin:/usr/bin:/opt/puppetlabs/bin)  
/bin/dnf  
/bin/yum  
/usr/bin/which: no pacman in (/sbin:/bin:/usr/sbin:/usr/bin:/opt/puppetlabs/bin)  
/usr/bin/which: no zypper in (/sbin:/bin:/usr/sbin:/usr/bin:/opt/puppetlabs/bin)
- To know the package version give **dnf --version**


## Package Types by Linux

| Distro                | Package manager | Package file   |
| --------------------- | --------------- | -------------- |
| Ubuntu / Debian/ Mint | `apt`           | `.deb`         |
| RHEL / CentOS / Fedora| `dnf` / `yum`   | `.rpm`         |
| SUSE                  | `zypper`        | `.rpm`         |
| Arch Linux            | `pacman`        | `.pkg.tar.zst` |
| Alpine                | `apk`           | `.apk`         |


1. **APT (Advanced Package Tool)**  
Used in Debian – based distributions like ubuntu, Mint. It works with '.deb' package files. To perform these tasks, we need to be root user.
- sudo apt install `<package-name>`  # installs a package
- sudo apt remove `<package-name>`   # removes a package
- sudo apt update `<package-name>`   # refresh package lists
- sudo apt upgrade `<package-name>`  # upgrades all installed packages
- sudo apt update && sudo apt upgrade # refresh and upgrades packages

2. **DNF (Dandified YUM/ YUM – Yellodog Updater, Modified)**  
Used in Red Hat – based distributions like Federo, CentOS. They work with '.rpm' package files. DNF is modern successor to YUM.
### dnf
- sudo dnf update
- sudo dnf install `<package-name>`
- sudo dnf remove `<package-name>`
### yum
- sudo yum install `<package-name>`
- sudo yum remove `<package-name>`
- sudo yum update `<package-name>`
- sudo yum info `<package-name>`
- sudo yum list available     # checks in the repository that we have connected
- sudo yum list installed     # checks for the packages installed in local system

3. **Pacman**  
Used in Arch Linux and its derivatives like Manjaro. It’s known for its speed and efficiency. They work with '.pkg.tar.zst' package files.
- sudo pacman -Syy                 # refresh packages
- sudo pacman -Syn                 # upgrade packages
- sudo pacman -S `<package-name>`  # install packages
- sudo pacman -Rs `<package-name>` # removes packages
