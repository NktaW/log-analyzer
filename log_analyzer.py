"""Analyze Linux authentication logs."""

import sys

LOG_FILE = "/var/log/auth.log"


def read_lines(path):
    """Read a log file and return its lines."""
    try:
        with open(path, encoding="utf-8", errors="replace") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: permission denied: {path}", file=sys.stderr)
        sys.exit(1)


def main():
    """Run the log analysis."""
    lines = read_lines(LOG_FILE)
    print(f"Read {len(lines)} lines from {LOG_FILE}")


if __name__ == "__main__":
    main()
