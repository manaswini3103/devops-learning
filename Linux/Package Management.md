# Package Management
Package managers streamline the installation, update and removal of software. Each distribution uses its own package management system. These are software tools designed to automate these tasks and manage dependencies.

1. **APT (Advanced Package Tool)**  
Used in Debian – based distributions like ubuntu, Mint, Debian. It works with .deb package files. To perform these tasks, we need to be root user.
- sudo apt install `<package-name>`  # installs a package
- sudo apt install `<package-name>`  # installs a package
- sudo apt remove `<package-name>`   # removes a package
- sudo apt update `<package-name>`   # refresh package lists
- sudo apt upgrade `<package-name>`  # upgrades all installed packages
- sudo apt update && sudo apt upgrade # refresh and upgrades packages

2. **DNF (Dandified YUM/ YUM – Yellodog Updater, Modified)**  
Used in Red Hat – based distributions like Federo, CentOS. They work with .rpm package files. DNF is modern successor to YUM.
- sudo dnf update
- sudo dnf install `<package-name>`
- sudo dnf remove `<package-name>`

- sudo yum install `<package-name>`
- sudo yum remove `<package-name>`
- sudo yum update `<package-name>`
- sudo yum info `<package-name>`
- sudo yum list available     # checks in the repository that we have connected
- sudo yum list installed     # checks for the packages installed in local system

3. **Pacman**  
Used in Arch Linux and its derivatives like Manjaro. It’s known for its speed and efficiency.
- sudo pacman -Syy                 # refresh packages
- sudo pacman -Syn                 # upgrade packages
- sudo pacman -S `<package-name>`  # install packages
- sudo pacman -Rs `<package-name>` # removes packages
