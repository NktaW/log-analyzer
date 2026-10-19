# Log Analyzer

A small Python script that reads an SSH authentication log and summarizes failed login attempts.

> **Status: work in progress.** This is a learning project, and only part of the planned functionality is implemented.

## What works now

- Reads a log file whose path is given as a command-line argument
- Handles common errors (missing file, permission denied, missing or extra arguments) and exits with a non-zero exit code

## Planned (not implemented yet)

- Detect failed SSH password attempts
- Count attempts per IP address and show the most active ones
- List the usernames that were tried
- Print a summary to the terminal

## Requirements

- Python 3 (standard library only, no extra packages)
- Developed and tested on Ubuntu only

## Usage

```bash
python3 log_analyzer.py samples/auth_sample.txt
```

The script only reads the file. Do not run it with `sudo`.

## Test data

This repository does not contain any real log data. `samples/auth_sample.txt` is a synthetic log written by hand. It uses IP addresses from the documentation ranges reserved in RFC 5737 (for example 203.0.113.0/24) and invented user and host names.

## Design notes

- Log content is treated as untrusted input, because parts of it (such as the username in a failed login) can be controlled by an attacker.
