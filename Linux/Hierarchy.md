# Linux Directory Hierarchy

In Linux, everything is organized in a single tree-like structure that starts from the **root directory (/)**.  
All directories and files appear under it as branches.

---

## Important Directories in Linux

- **/** – The root directory (similar to `C:\` in Windows)
- **/root** – Home directory for the root (administrative) user
- **/home** – Home directories for regular users
- **/usr** – Default location where software is installed (similar to `C:\Program Files`)
- **/bin** – Essential commands used by all users
- **/sbin** – Commands used by superusers (system binaries)
- **/var** – Variable data such as mail, logs, spool files
- **/etc** – System configuration files
- **/lib** – Shared libraries and kernel modules
- **/dev** – Device files
- **/tmp** – Temporary files
- **/media** – Mount point for removable storage devices

---

## Configuration Files

Configuration files are typically plain-text files that contain instructions, settings, and values for programs, utilities, and system processes.

### Common Examples:

- **/etc/fstab** – Defines file systems to be mounted at boot  
- **/etc/network/interfaces** *(or Netplan YAML files on newer systems)* – Configures network interfaces  
- **/etc/ssh/sshd_config** – Configuration for the SSH daemon  
- **Application-specific configuration files**, e.g.:  
  - `~/.bashrc` – User-specific shell settings

