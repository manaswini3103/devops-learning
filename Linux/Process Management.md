# Process Management
- When you start a program or run an application in Linux, it runs as a program.
- A Linux process (a daemon), running in foreground or in the background uses memory and CPU resources.

**Command**                            **Description**  
**ps -ef**                      list the process which are running in the system  
                                e – show every process of all users  
                                f – use full format listing      
**kill/kill -9**                kills a process or service  
**fg**                          run the program in foreground ex: fg %1  
**bg**                          runs the service in the back group ex: bg %2  
**top**                         list top 20 process which are consuming more CPU  
- ps -ef: like task manager
[root@omega html]# ps -ef
UID         PID   PPID  C STIME TTY          TIME CMD
root          1      0  0  2024 ?        05:27:32 /usr/lib/systemd/systemd –switched
root --system --deserialize 22
root          2      0  0  2024 ?        00:00:09 [kthreadd]
root          6      2  0  2024 ?        00:55:52 [ksoftirqd/0]
- PPID is the parent process ID, PID – process ID, whenever a user is logged in a PID will be created.
- if we want to get the informationfor particular process, give
ex: ps -ef | grep ssh
- If we want to stop the service, we can give “service http stop”, but if it’s still not stopped. Then we can go for kill option
ex: kill PID
    kill -9 PID
