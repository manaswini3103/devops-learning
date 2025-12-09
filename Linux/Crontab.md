# Crontab
- In any operating system, it is possible to create jobs that you want to reoccur.
- This process is known as job scheduling, it is usually done based on user-defined jobs.
- For RedHat or any other Linux, this process is handled by the cron service or a daemon called “crond”, which can be used to schedule tasks.
- Each user can create a cron job.

| Field | Description        | Allowed Value |
|-------|---------------------|----------------|
| MIN   | Minute field        | 0 to 59        |
| HOUR  | Hour field          | 0 to 23        |
| DOM   | Day of the month    | 1–31           |
| MON   | Month field         | 1–12           |
| DOW   | Day of the week     | 0–6            |
| CMD   | Any command         | —              |


## commands
**crontab -l** (lists the cron jobs running)<br>
**crontab -e** (we can add a cron job using this command where e – edit)
**crontab -r** (If you want to remove every cron job for the current user, without any confirmation)
**crontab -i -r** (this gives safety prompt before removing)

- Execute a job at 8:30 on everyday morning
**ex**: 30 8 * * * command
min - 30, hour – 8, dom – all days(*), month - *, dow - *
**ex**: 30 08 * * * echo “1” >> /tmp/file1
print 1 to /tpmp/file1 everyday at 8:30 AM
- Execute a job at 2:00 PM every Saturday
**ex**: 00 12 * * 6 command
min – 0, hour – 12(2PM), dom - *, month - *, dow – 6(Saturday)
- Execute a job at 12:00 AM on 1st July
**ex**: 00 00 01 07 * command
- Execute a job at 3:30 PM on every month 25th
**ex**: 30 15 25 * * command
- If we want do a job every minute
**ex**: * * * * * command
