# System Management:

history         – list all commands executed by user
free            - tells how much frees memory is there in a server
/proc/meminfo   – displays memory information
/proc/cpuinfo   - displays CPU info
uname -a        - show kernal info
du              – show directory usage
whereis         - shows possible locations of app
which           - show which app will be run by default
df              - disk free, how many file systems are there in our system

- When we give ls -la we’ll be able to find the hidden files, in that we’ll find .bash_history, because of which we find all the history commands.
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
