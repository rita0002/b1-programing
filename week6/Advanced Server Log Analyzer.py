import re
import logging
from datetime import datetime
from collections import defaultdict, Counter

# Setup logging for audit trail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("analysis_audit.log"),
        logging.StreamHandler()
    ]
)

class ServerLogAnalyzer:
    """A simple server log analyzer for traffic and security reporting."""

    def __init__(self, log_file):
        self.log_file = log_file
        # Regex to parse Apache-style logs
        self.log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+)')

        # Statistics
        self.total_requests = 0
        self.unique_ips = set()
        self.methods_count = Counter()
        self.urls_count = Counter()
        self.status_count = Counter()
        self.errors = []

        # Security tracking
        self.failed_logins = defaultdict(list)
        self.forbidden_access = []
        self.security_incidents = []

    def parse_line(self, line):
        """Parse a single log line into a structured dictionary."""
        match = self.log_pattern.match(line)
        if not match:
            logging.debug(f"Malformed line skipped: {line}")
            return None
        ip, timestamp, method, url, status, size = match.groups()
        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "url": url,
            "status": int(status),
            "size": int(size)
        }

    def analyze_security(self, entry):
        """Identify security events from a log entry."""
        # Failed login attempts
        if entry["url"] == "/login" and entry["status"] == 401:
            self.failed_logins[entry["ip"]].append(entry["timestamp"])
            if len(self.failed_logins[entry["ip"]]) >= 3:
                incident = f"Brute force from {entry['ip']} ({len(self.failed_logins[entry['ip']])} failures)"
                self.security_incidents.append(incident)
                logging.warning(incident)

        # Forbidden access
        if entry["status"] == 403:
            incident = f"Forbidden access: {entry['ip']} -> {entry['url']}"
            self.forbidden_access.append(incident)
            self.security_incidents.append(incident)
            logging.warning(incident)

        # Potential SQL injection
        sql_patterns = ["union", "select", "drop", "insert", "--", ";"]
        if any(pat in entry["url"].lower() for pat in sql_patterns):
            incident = f"Potential SQL injection: {entry['ip']} -> {entry['url']}"
            self.security_incidents.append(incident)
            logging.warning(incident)

    def process_logs(self):
        """Read the log file line by line and analyze."""
        try:
            logging.info(f"Analyzing log file: {self.log_file}")
            with open(self.log_file, "r") as f:
                for line_num, line in enumerate(f, start=1):
                    try:
                        entry = self.parse_line(line.strip())
                        if not entry:
                            continue

                        # Update statistics
                        self.total_requests += 1
                        self.unique_ips.add(entry["ip"])
                        self.methods_count[entry["method"]] += 1
                        self.urls_count[entry["url"]] += 1
                        self.status_count[entry["status"]] += 1

                        # Track errors
                        if entry["status"] >= 400:
                            self.errors.append(entry)

                        # Security checks
                        self.analyze_security(entry)
                    except Exception as e:
                        logging.error(f"Line {line_num} processing error: {e}")
                        continue
            logging.info(f"Finished processing {self.total_requests} requests")
        except FileNotFoundError:
            logging.error(f"Log file not found: {self.log_file}")
        except PermissionError:
            logging.error(f"Permission denied reading: {self.log_file}")

    def generate_summary_report(self):
        """Create summary report for traffic and requests."""
        try:
            with open("summary_report.txt", "w") as f:
                f.write("="*60 + "\n")
                f.write("SERVER LOG SUMMARY\n")
                f.write("="*60 + "\n\n")
                f.write(f"Total Requests: {self.total_requests}\n")
                f.write(f"Unique Visitors: {len(self.unique_ips)}\n\n")

                f.write("HTTP Methods:\n")
                for method, count in self.methods_count.most_common():
                    f.write(f"  {method}: {count}\n")

                f.write("\nTop 5 Requested URLs:\n")
                for url, count in self.urls_count.most_common(5):
                    f.write(f"  {url}: {count}\n")

                f.write("\nStatus Codes:\n")
                for status, count in sorted(self.status_count.items()):
                    f.write(f"  {status}: {count}\n")
            logging.info("Summary report generated")
        except PermissionError:
            logging.error("Cannot write summary_report.txt")

    def generate_security_report(self):
        """Create security incidents report."""
        try:
            with open("security_incidents.txt", "w") as f:
                f.write("="*60 + "\n")
                f.write("SECURITY INCIDENTS\n")
                f.write("="*60 + "\n\n")
                f.write(f"Total Security Incidents: {len(self.security_incidents)}\n\n")

                f.write("Brute Force Attempts:\n")
                for ip, attempts in self.failed_logins.items():
                    if len(attempts) >= 3:
                        f.write(f"IP: {ip} - {len(attempts)} failed logins\n")

                f.write("\nForbidden Access Attempts:\n")
                for incident in self.forbidden_access:
                    f.write(f"{incident}\n")

                f.write("\nAll Security Incidents:\n")
                for incident in self.security_incidents:
                    f.write(f"{incident}\n")
            logging.info("Security report generated")
        except PermissionError:
            logging.error("Cannot write security_incidents.txt")

    def generate_error_log(self):
        """Generate error log file for 4xx and 5xx responses."""
        try:
            with open("error_log.txt", "w") as f:
                f.write("="*60 + "\n")
                f.write("HTTP ERRORS\n")
                f.write("="*60 + "\n\n")
                f.write(f"Total Errors: {len(self.errors)}\n\n")
                for err in self.errors:
                    f.write(f"[{err['timestamp']}] {err['ip']} - {err['method']} {err['url']} - Status: {err['status']}\n")
            logging.info("Error log generated")
        except PermissionError:
            logging.error("Cannot write error_log.txt")


def main():
    analyzer = ServerLogAnalyzer("server.log")
    analyzer.process_logs()
    analyzer.generate_summary_report()
    analyzer.generate_security_report()
    analyzer.generate_error_log()

    print("\nAnalysis Complete!")
    print(f"Total Requests: {analyzer.total_requests}")
    print(f"Security Incidents: {len(analyzer.security_incidents)}")
    print(f"Errors Found: {len(analyzer.errors)}")
    print("\nReports generated:")
    print(" - summary_report.txt")
    print(" - security_incidents.txt")
    print(" - error_log.txt")
    print(" - analysis_audit.log")


if __name__ == "__main__":
    main()
