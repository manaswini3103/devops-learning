# Networking
Linux networking involves the configuration and management of network connectivity on a Linux-based system. This includes various aspects, from identifying and configuring network interfaces to managing IP addresses, routing, DNS, and firewalls.

## Key Components and Concepts
- **Network Interfaces**: These are the hardware or virtual components (e.g., Ethernet cards, Wi-Fi adapters) through which a Linux system connects to a network. Commands like ip link or ifconfig (older) are used to view and manage these interfaces.
- **IP Addressing**: Devices on a network are identified by IP addresses (IPv4 and IPv6). Configuration involves assigning IP addresses, subnet masks, and default gateways.
- **Routing**: This process directs data packets between different networks. Linux maintains routing tables to determine the best path for data. The ip route command is used to inspect and modify routing tables.
- **DNS (Domain Name System)**: DNS translates human-readable domain names (e.g., example.com) into IP addresses that computers can understand. DNS server settings are configured to enable this resolution.
- **Firewalls**: Tools like iptables or nftables are used to control network traffic by defining rules that permit or block connections, enhancing security. 
- **Network Services**: Various services support network operations, including DHCP (for dynamic IP address assignment), DNS servers, and network monitoring tools like arpwatch.
- **Virtual Networking**: Linux excels in virtual networking, providing capabilities for creating virtual interfaces, bridges, VLANs, and other constructs essential for virtualization and containerization environments.

## Common commands
1. **hostname** - list host name of server
- **ex**:
[root@omega chennasa]# hostname
omega
- The server info will be stored in /etc/hostname.
- We can update hostname vi /etc/hostname and give the name that we like.
- If we want the name that we have given in /etc/hostname to reflect as the        out of “hostname” command for that we need to restart the system by giving “init 6” or “reboot” command.
- If we want to change the hostname instantly, give “hostname name”.
- Now, if we give “hostname”, output would be the name that we have given.

2. **ping <ip>** - availability of destination server over the network.
- **ex**: ping google.com (it tells from this system if google.com is reachable or not.
[root@omega chennasa]# ping google.com
PING google.com (142.250.189.14) 56(84) bytes of data.
64 bytes from lax31s16-in-f14.1e100.net (142.250.189.14): icmp_seq=1 ttl=113 time=24.3 ms
64 bytes from lax31s16-in-f14.1e100.net (142.250.189.14): icmp_seq=2 ttl=113 time=24.3 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 5006ms
rtt min/avg/max/mdev = 24.274/24.313/24.354/0.130 ms
[root@omega chennasa]#
- google.com is a web application running on some server with IP (142.250.189.14)
- also when we try to gibe some random IP and check it’s availability
[root@omega chennasa]# ping 10.23.12.4
PING 10.23.12.4 (10.23.12.4) 56(84) bytes of data.
^C
--- 10.23.12.4 ping statistics ---
13 packets transmitted, 0 received, 100% packet loss, time 12000ms

3. **wget** - download packages/softwares onto linux system
**ex**:  wget link (copy the link of the thing that we want to install from browser)
when we list the files/directories in the path we have downloaded we can find it.
	
4. **ifconfig** - lists IP addresses of server/system
- we can even use “ip addr” command. We could have more than one IP, the highlighted one is the IP of the server.
 
5. **telnet** - connect to remote host/check port availability status
- each server will have one or more IP (unique number), for AWS EC2 instance we’ll have two IP’s one is public IP (if we want access it through internet) and priate IP (we can access it locally)
- In a server we can run one or more applications and each application should have a unique number called port number (port no.s range from 0 to 65k+).
- some services run on default port numbers.
port number           service            config
       21              FTP
       22              SSH         /etc/ssh/sshd_config
       23              TELNET
       25              SMTP
       53              DNS     
       80              HTTP        /etc/httpd/conf/httpd.conf
      443              HTTPS

**ex**: telnet localhost portnumber
 
6. **netstat** - If we want to check how many applications are running in our system and on which port it’s running, give the below command.
**ex**: netstat -tulpn
in the below screen shot, in state column if there is LISTEN, which means those ports are occupied and the blanks ones are free.

7. **curl** - access the application as from browser
- once if we deploy the application and wanted to check from our local system whether it is accessible or not.
[root@omega chennasa]# curl google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>

8. **SSH** – The SSH (secure Shell) protocol is a method for secure remote login from once computer to another. It provides several alternative options for strong authentication, and it protects the communications securely and integrity with strong encryption.
port number      : 22
Daemon/process   : sshd
Conf file        : /etc/ssh/sshd_config

**how it works** 
If we want to login from server1 to server2, we need key to login to it. We’ll have private (id is “id_rsa” stored in $HOME/.ssh/id_rsa) and public (id is “id_rsa.pub” stored in $HOME/.ssh/authorized_keys) keys. Anyone can know our public key but shouldn’t know our private key.

**Steps**
1. **how to generate key**
We generate key in server1
- #ssh-keygen (or) #ssh-keygen -t rsa -b 4096/2048
- keys are generated in .ssh dir under user’s home directory.
2. **where to store it**
- We will copy the public key from Server1 to Server2 in the .ssh directory (file: authorized_keys) under the user’s home directory. This can be done in two ways:
   1. Manually:
Open the authorized_keys file on Server2 using vi and paste the public key from Server1:
vi $HOME /.ssh/authorized_keys
here $HOME is the user, if we want the key to be copied to /root user then the name should be “$ROOT/.ssh/authorized_keys”.
   2. Using ssh-copy-id:
Run the following command from Server1 to copy the public key automatically:
ssh-copy-id <IP_Address_of_Server2>
3. **how to use it**
- If you want to login to server2 from server1, it checks the current servers (server1) private key and try to match with another server (server2) public key.
- And if they same make a pair of private and public keys then it’ll allow to login to another server.
#ssh -I <key_location> username@<ip_address>
#ssh <target-server-ip>
ex: ssh -i /root/.ssh/id_rsa root@ip-add

9. **SCP** – SCP(secure copy) is a command-line utility that allows you to securely copy files and directories between two systems/servers.
- for Windows to Linux copying we use tools such as “Mobaxterm” or “winscp”
- for Linux to Linx
**syn**: scp source_file_name username@destination_host:destination_folder
**ex**: scp file1 root@10.20.30.40:/tmp/
      scp root@10.20.30.40:/tmp/file2 /home/ec2-user/
      scp -r src root@10.20.30.40:/tmp/ (-r : for copying directories)
