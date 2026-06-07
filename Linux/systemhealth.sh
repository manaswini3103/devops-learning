# System Health Reporter
# Display: hostname, uptime, CPU usage, memory usage, disk usage 
# Output to both console and log file with timestamp 
# sColor-coded output (green: healthy, yellow: warning, red: critical) 

#!/bin/bash # Tells the system to run this script using Bash.

LOG_FILE="/var/log/system_health.log" # where output is saved
# Run date (Linux command that prints date/time), format it nicely, and store it in variable called TIMESTAMP
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# Color codes
GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[31m"
NC="\e[0m"   # No color

log() {
    echo -e "[$TIMESTAMP] $1" | tee -a "$LOG_FILE"
}
# echo -e → prints text (-e: Enable escape sequences (colors, \n - next line))
# $1 : means the first argument passed to function/something
# tee -a → shows output on the terminal and appends (-a) the same output to the log file


colorize() {
    # local variables are defined with keyword 'local'
    local value=$1 # first argument
    local warn=$2 # Second argument
    local crit=$3 # Third argument

    # -eq: Equal, -ge: Greater Than or Equal, -gt: Greater Than, -le: Less Than or Equal, -lt: Less Than, -ne: Not Equal

    if [ "$value" -ge "$crit" ]; then 
        echo -e "${RED}${value}%${NC}"
    elif [ "$value" -ge "$warn" ]; then
        echo -e "${YELLOW}${value}%${NC}"
    else
        echo -e "${GREEN}${value}%${NC}"
    fi # keyword that ends if block
}

log "================ SYSTEM HEALTH CHECK ================"

# Hostname
HOSTNAME=$(hostname) # Run hostname linux command and save the output/result in a variable called HOSTNAME, $(...) = command substitution
log "Hostname        : $HOSTNAME"
# calling the function 'log' that we created earlier, so "Hostname : $HOSTNAME" becomes first argument $1
# the output would be like "[2026-02-01 15:45:12] Hostname        : prod-server-01"

# Uptime
UPTIME=$(uptime -p)
# uptime linux command shows how long system has been running since last boot, output: "16:45:12 up 5 days, 2:13,  2 users,  load average: 0.08, 0.12, 0.10"
# -p: pretty format, output: "up 5 days, 2 hours, 13 minutes"
log "Uptime          : $UPTIME"

# CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print int(100 - $8)}')
# top: shows running processes & CPU stats, -b → batch mode (non-interactive), -n1 → run once, not continuously
# grep "Cpu(s)": Filters only the CPU line.
# $8 field maens 'id' → idle CPU percentage, if idle = 90.7, then 100 - idle = 100 - 90.7 = 9.3, int(): removes decimal parts, result is 9
CPU_COLORED=$(colorize "$CPU_USAGE" 60 85)
log "CPU Usage       : $CPU_COLORED" # output: [2026-02-01 16:10:01] CPU Usage       : 9%

# Memory usage
MEM_USAGE=$(free | awk '/Mem:/ {printf("%d"), $3/$2 * 100}')
# free: shows memory usage including total, used amd free memory, printf("%d"): print as integer 
# awk '/Mem:/ { ... }': Selects only the line starting with Mem, $2: total memory, $3: used memory, 3120 / 7977 * 100 = 39%, result = 39
MEM_COLORED=$(colorize "$MEM_USAGE" 70 90)
log "Memory Usage    : $MEM_COLORED"

# Disk usage (root filesystem)
DISK_USAGE=$(df / | awk 'NR==2 {gsub("%",""); print $5}')
# df /: Shows disk usage for the root filesystem. NR = record (line) number, line 2 contains actual values
# print $5: print fifth column which has disk usage percentage, gsub("%",""): substituting percentage with nothing
DISK_COLORED=$(colorize "$DISK_USAGE" 75 90)
log "Disk Usage (/)  : $DISK_COLORED"

log "====================================================="
echo
