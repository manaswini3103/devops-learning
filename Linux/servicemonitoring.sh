#!/bin/bash

# Services to monitor
SERVICES=("nginx" "docker")

# Log file
LOG_FILE="/var/log/service_monitor.log"

# Alert email (change or remove if you prefer Slack/webhook)
ALERT_EMAIL="admin@example.com"

timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

log() {
  echo "$(timestamp) - $1" >> "$LOG_FILE" # if we call the function like "log nginx", the output would be "2026-02-01 12:45:03 - nginx" stored in log file value
}

alert() { # -s: email subject (subject: Service Restart Alert on prod-server-01), $ALERT_EMAIL=recipient
  echo "$1" | mail -s "Service Restart Alert on $(hostname)" "$ALERT_EMAIL"
}
# if we call the function (alert "nginx was down and restarted"), Body: nginx was down and restarted

for SERVICE in "${SERVICES[@]}"; do # we took 2 services (docker, nginx), it will iterate one after the other
  
  # if docker and nginx is not installed it'll throw error like 
  # "Failed to restart docker.service: Unit docker.service not found", to avoid this error we'll write the below if block
  if ! systemctl list-unit-files | grep -q "^$SERVICE.service"; then
  # systemctl list-unit-files: prints all known service unit files which are installed (enabled or disabled)
  # grep -q "^$SERVICE.service": serches for the service starting with the given name, -q: runs in quet mode, example: grep -q "^docker.service"
  # ! : if block executes only when service is not found.
    log "$SERVICE service is not installed. Skipping."
    continue
  fi

  if systemctl is-active --quiet "$SERVICE"; then # returns exit code 0 if running, returns non-zero if not running
    log "$SERVICE is running" # output: "2026-02-01 12:45:03 - docker is running"
  else
    log "$SERVICE is NOT running. Attempting restart..."
    systemctl restart "$SERVICE" # Attempts to restart the service

    sleep 2 # Gives service time to actually start before re-checking. Without this, you can get false negatives

    if systemctl is-active --quiet "$SERVICE"; then
      log "$SERVICE restarted successfully"
      alert "$SERVICE was down and has been restarted on $(hostname) at $(timestamp)"
    else
      log "FAILED to restart $SERVICE"
      alert "CRITICAL: $SERVICE is DOWN and could not be restarted on $(hostname)"
    fi
  fi
done
