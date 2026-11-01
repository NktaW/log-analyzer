"""Analyze Linux authentication logs."""

import sys


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


def is_failed_login(line):
    """Return True if the line is a failed SSH password attempt."""
    if ": " not in line:
        return False
    header, message = line.split(": ", 1)
    return " sshd[" in header and message.startswith("Failed password for ")


def main():
    """Run the log analysis."""
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <log_file>", file=sys.stderr)
        sys.exit(2)

    log_file = sys.argv[1]
    lines = read_lines(log_file)
    print(f"Read {len(lines)} lines from {log_file}")
    failed_lines = []
    for line in lines:
        if is_failed_login(line):
            failed_lines.append(line)
    print(f"Found {len(failed_lines)} failed login attempts")


if __name__ == "__main__":
    main()
