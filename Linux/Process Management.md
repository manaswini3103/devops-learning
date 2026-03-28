# Process Management
- Process management is the OS making sure many programs can run at the same time without chaos. It starts programs, keeps them running, shares CPU & memory between them and stops them when needed.
- **Process** A running instance of a program  
  Example:  
  - Program: firefox
  - When you open it → it becomes a process
  - Open it again → another process
- A Linux process (a daemon), **Daemon** - a background program that runs quietly and continuously to provide a service, it waits to do work when needed and uses memory and CPU resources.
  - It starts at boot time, runs continuously, lives in **/usr/sbin/ or /sbin/**
  -  To see running Daemons **ps -ef | grep d**, where 'd' is Daemon
  - Listens for: network requests, system events, scheduled times. 
  - Responds when something happens
    Example:
    - sshd sleeps in the background  
    - You try to SSH in  
    - sshd wakes up and handles it  

**Commands**  
- **ps -ef** : list the process which are running in the system, where 'e' – show every process of all users and 'f' – use full format listing.
  [root@omega html]# ps -ef  
  UID         PID   PPID  C STIME TTY          TIME CMD    
  root          1      0  0  2024 ?        05:27:32 /usr/lib/systemd/systemd –switched  
  root --system --deserialize 22  
  root          2      0  0  2024 ?        00:00:09 [kthreadd]  
  root          6      2  0  2024 ?        00:55:52 [ksoftirqd/0]
  - PPID is the parent process ID, PID – process ID, whenever a user is logged in, a PID will be created.
  - PID 1 → systemd, systemd starts other processes, those start more processes which forms a process tree.
  - if we want to get the information for particular process give **ps -ef | grep ssh**
  - If we want to stop the service, we can give “service http stop”, but if it’s still not stopped. Then we can go for kill option  
  ex: kill PID  
      kill -9 PID
- **kill/kill -9**: kills a process or service  
- **fg**: run the program in foreground, ex: fg %1  
- **bg**: runs the service in the back group ex: bg %2  
- **top**: list top 20 process which are consuming more CPU
