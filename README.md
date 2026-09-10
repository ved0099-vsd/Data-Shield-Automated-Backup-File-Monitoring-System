# Data Shield – Automated Backup & File Monitoring System

A Python-based automation system designed to monitor files and directories, detect changes, and maintain automated backups of important data.

## Features

- Monitors files and directories for changes.
- Detects newly added or modified files.
- Uses checksum-based file comparison.
- Creates automated backups of important data.
- Synchronizes modified or newly added files.
- Maintains backup records and logs.
- Supports periodic automated execution.
- Creates compressed backup archives.
- Helps protect important files from accidental data loss.

## Technologies Used

- Python
- OS Module
- Sys Module
- Time Module
- Schedule Module
- Hashlib
- Shutil

## Project Components

### Directory Traversal

Recursively scans directories and their subdirectories to identify files that need to be monitored or backed up.

### Checksum-Based Monitoring

Calculates file checksums to compare files and identify whether their contents have changed.

### File Backup

Automatically creates copies of important files and maintains them in a backup location.

### Change Detection

Detects newly created or modified files by comparing their current state with previously recorded information.

### Scheduling

Uses the Schedule module to perform backup and monitoring operations periodically without requiring manual execution.

### Backup Archive

Organizes backup data and supports compressed archive creation for easier storage and management.

## How to Run

Run the required Python script from the command line.

Example:

```bash
python FileName.py DirectoryName

Replace FileName.py with the required script and DirectoryName with the directory you want to monitor or back up.

Usage

To monitor a directory, provide its path as a command-line argument.

Example:

python DirectoryScanner1.py "C:\Path\To\Test"
Backup and Monitoring

The system scans the specified directory, compares files using checksums, identifies newly added or modified files, and performs the required backup operations.

Project Type

Python Automation / Backup & File Monitoring Project

Author

Ved Dhamal
