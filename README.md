# File Integrity Monitor

A Python-based File Integrity Monitor (FIM) that watches for changes (creation, modification, deletion) in a specified directory. Whenever changes occur, it logs them, calculates and compares file hashes, and can optionally send email/SMS alerts.

---

## Features

- **Real-Time Monitoring**: Uses the [`watchdog`](https://pypi.org/project/watchdog/) library to detect file system changes instantly.  
- **Hash Comparison**: Employs Python’s built-in `hashlib` to compute and compare file hashes, detecting unauthorized modifications.  
- **Logging**: Writes events to a `logs/integrity.log` file for easy review.  
- **Optional Alerts**: Potential to integrate email or SMS notifications (via `smtplib` or `twilio`) on critical changes.  
- **Easy Setup**: Simple Python scripts with no external dependencies beyond `watchdog` (and optionally `twilio`).

---

## Installation

1. **Clone or Download** this repository.
2. **Install Python 3.8+** (if not already).
   - Check with:  
     ```bash
     python --version
     ```
3. **(Optional) Create a virtual environment** (recommended):
   ```bash
   python -m venv venv


## Troubleshooting 

Too Many Log Entries:
You might be monitoring your entire project folder (including your venv and logs directory). Update folder_to_monitor to point only to the folder with the files you actually want to monitor.

Permission Errors:
On some systems, you may need additional permissions to read/monitor certain directories.

Virtual Environment Issues:
Make sure you activate the environment before installing packages (watchdog, etc.) so they install in the correct location.
