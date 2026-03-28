# Log Files and Troubleshooting
- Log management is the process of collecting, storing, analyzing, and rotating logs. It helps administrators keep track of system events, while ensuring that old logs are safely archived or removed.
- Logs will be stored in /var/log it’s the main path.

## Common Log Files in Linux
- **/var/log/syslog**  : General system messages and events.
- **/var/log/auth.log**: Authentication and login-related events.
- **/var/log/kern.log**: Kernel-related messages.
- **/var/log/boot.log**: Boot-time messages.
- **/var/log/dmesg**   : Hardware and kernel ring buffer messages.

## Log Management Tools in Linux
Linux provides several built-in tools to manage logs effectively:
1. **syslog**   : The standard for logging system messages.
2. **rsyslog**  : An enhanced version of syslog with better performance and filtering.
3. **systemd journal** : a centralized logging system used by Linux systems to collect, store, and manage logs.
4. **journald** : a background service (daemon) which runs automatically as part of systemd. Collects logs from: Kernel, System services, Applications, Stdout / stderr. Stores them in the systemd journal and adds metadata (PID, UID, service name, boot ID, etc.). we don’t “run” this manually, we can check it like this: **systemctl status systemd-journald**
5. **journalctl** : a command-line tool used by admins/users to query and view logs written by 'journald'
6. **logrotate**: A tool for managing log file rotation, compression, and archiving.

## journald vs journalctl

| Feature            | journald             | journalctl            |
| ------------------ | -------------------- | --------------------- |
| Type               | Daemon (service)     | CLI command           |
| Role               | Writes & stores logs | Reads & displays logs |
| Runs in background | ✅                   | ❌                   |
| Collects logs      | ✅                   | ❌                   |
| Queries logs       | ❌                   | ✅                   |
| Needs sudo         | N/A                  | Often yes             |


## Managing Files in Logs
1.	cat /var/log/syslog, cat /var/log/auth.log
2.	grep “FAILED” /var/log/auth.log
3.	sort /var/log/kern.log (sorts in alphabetical or numcerical ways, ex considers and displays latest date and time logs.)
4.	journalctl
**syn**: journalctl [options] [unit]  
**ex**:
- sudo journalctl -r               (to reverse the order)  
- sudo journalctl -n 2             (displays 2 log entries)  
- sudo journalctl | grep Centaur   (filtering by keyword)  
- sudo journalctl -u apache2       (filtering by specific user)
- sudo journalctl -b (Show logs from the current boot only)
- sudo journalctl -b -1 (Show logs from previous boot)
- journalctl --help                (help section of journalctl)  
- journalctl -p warning            (display on desired priority level ex emerg, alert, err, info, warning, notice, etc)
- sudo journalctl -b -p err (for errors only)
- sudo journalctl -b -p warning (warnings + errors)
