# Log Files and Troubleshooting
- Log management is the process of collecting, storing, analyzing, and rotating logs. It helps administrators keep track of system events, while ensuring that old logs are safely archived or removed.
- Logs will be stored in /var/log it’s the mail path.

## Common Log Files in Linux
**/var/log/syslog**  : General system messages and events.
**/var/log/auth.log**: Authentication and login-related events.
**/var/log/kern.log**: Kernel-related messages.
**/var/log/boot.log**: Boot-time messages.
**/var/log/dmesg**   : Hardware and kernel ring buffer messages.

## Log Management Tools in Linux
Linux provides several built-in tools to manage logs effectively:
1. syslog   : The standard for logging system messages.
2. rsyslog  : An enhanced version of syslog with better performance and filtering.
3. journald : Part of systemd, responsible for structured log storage and retrieval.
4. logrotate: A tool for managing log file rotation, compression, and archiving.

## Managing Files in Logs
1.	cat /var/log/syslog, cat /var/log/auth.log
2.	grep “FAILED” /var/log/auth.log
3.	sort /var/log/kern.log (sorts in alphabetical or numcerical ways, ex considers and displays latest date and time logs.)
4.	journalctl (used to view and manage system logs)
**syn**: journalctl [options] [unit]
**ex**:
sudo journalctl -r               (to reverse the order)
sudo journalctl -n 2             (displays 2 log entries)
sudo journalctl | grep Centaur   (filtering by keyword)
sudo journalctl -u apache2       (filtering by specific user)
journalctl --help                (help section of journalctl)
journalctl -p warning            (display on  desired priority level ex emerg, alert, err, info, warning, notice, etc)
