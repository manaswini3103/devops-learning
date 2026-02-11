# Linux Directory Hierarchy

In Linux, everything is organized in a single tree-like structure that starts from the **root directory (/)**.  
All directories and files appear under it as branches.

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

## Configuration Files
Configuration files are typically plain-text files that contain instructions, settings, and values for programs, utilities, and system processes.

### Common Examples:
- **/etc/hosts** - tells your system “when I type this hostname, use this IP address from /etc/hosts, it was checked before DNS.  
```bash
# cat /etc/hosts
127.0.0.1 localhost localhost.localdomain localhost4 localhost4.localdomain4
139.126.109.185 c04ppscnv829.ds.ad.adp.com c04ppscnv829
```  
where 127.0.0.1 → loopback (this machine), multiple aliases for localhost and used internally by system.  
system believes this IP (139.126.109.184) belongs to hostname c04ppscnv829 and its FQDN (Fully Qualified Domain Name is exact name of a computer or service on a network including its domain. It uniquely identifies a host on internet or a private network) is c04ppscnv829.ds.ad.adp.com
- **/etc/fstab** – Defines file systems to be mounted at boot  
- **/etc/network/interfaces** *(or Netplan YAML files on newer systems)* – Configures network interfaces  
- **/etc/ssh/sshd_config** – Configuration for the SSH daemon  
- **Application-specific configuration files**
ex:  `~/.bashrc` – User-specific shell settings

