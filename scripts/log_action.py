"""
log_action.py - Shared logging utility for Python scripts
Appends an entry to automation/movement_log.md

Usage:
    from log_action import log_action
    log_action("MAINTENANCE", source="-", destination="03_Mart/", notes="Cleaned Anki IDs")
"""

import os
from datetime import datetime

MOVEMENT_LOG = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "automation",
    "movement_log.md"
)


def log_action(operation, source="-", destination="-", status="Success", notes="-"):
    """Append a single row to movement_log.md."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"| {timestamp} | {operation} | {source} | {destination} | {status} | {notes} |\n"

    with open(MOVEMENT_LOG, "a", encoding="utf-8") as f:
        f.write(entry)
