#!/bin/bash
# log_action.sh - Shared logging utility for shell scripts
# Appends an entry to automation/movement_log.md
#
# Usage: source scripts/log_action.sh
#        log_action "OPERATION" "Source" "Destination" "Status" "Notes"
#
# Example: log_action "MAINTENANCE" "-" "03_Mart/" "Success" "Fixed CRLF -> LF"

MOVEMENT_LOG="./automation/movement_log.md"

log_action() {
    local operation="$1"
    local source="${2:--}"
    local destination="${3:--}"
    local status="${4:-Success}"
    local notes="${5:--}"
    local timestamp
    timestamp=$(date '+%Y-%m-%d %H:%M')

    echo "| ${timestamp} | ${operation} | ${source} | ${destination} | ${status} | ${notes} |" >> "$MOVEMENT_LOG"
}
