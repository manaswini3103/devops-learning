# System Management

System management is taking care of the OS, so users and applications can work smoothly.

## Basic Commands

1. history         : list all commands executed by user
2. free            : tells how much frees memory is there in a server
3. /proc/meminfo   : displays memory information
4. /proc/cpuinfo   : displays CPU info
5. uname -a        : show kernal info
6. du              : show directory usage
7. whereis         : shows possible locations of app
8. which           : show which app will be run by default
9. df              : disk free, how many file systems are there in our system

- When we give **ls -la** we’ll be able to find the hidden files, in that we’ll find .bash_history, because of which we find all the history commands.
- [root@omega chennasa]# free (may be the size is in KB)  
total        used        free      shared  buff/cache   available  
Mem:       16247608      961204      427884       39640    14858520    15113924  
Swap:       4194300     1981816     2212484  
[root@omega chennasa]# free -m (it’ll display in MB)
- [root@omega chennasa]# whereis ls  
ls: /usr/bin/ls /usr/share/man/man1/ls.1.gz  
- [root@omega chennasa]# which ls  
alias ls='ls --color=auto'  
/bin/ls  
[root@omega chennasa]#
