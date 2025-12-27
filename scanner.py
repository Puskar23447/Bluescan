import subprocess
from datetime import datetime
import time

target = "192.168.1.1-20"

risky_services = {
"ftp": "FTP is insecure. Use SFTP.",
"telnet": "Telnet is insecure. Disable it.",
"ssh": "SSH should use strong password.",
"http": "HTTP is unencrypted. use HTTPS.",
}

def progress_bar():
    print("Scanning Network: ",
end="", flush=True)
    for i in range(10):
        print("=", end="",
flush=True)
        time.sleep(0.1)
    print(" Done\n")

print("Starting Network Vulnerability Scan...")
progress_bar()

command = ["nmap", "-sV", "-T4", target]
result = subprocess.run(command, capture_output=True, text=True)
scan_output = result.stdout

report_file = f"reports/scan_report_{datetime.now().strftime('%y%m%d_%H%M%S')}.txt"
with open(report_file, "w") as file:
    file.write("Network Vulnerability Scan Report\n")
    file.write("--------------------------------\n\n")
    file.write(scan_output)
    file.write("\n\nSecurity Findings:\n")

    for service in risky_services:
        if service in scan_output.lower():
            file.write(f"\nService: {service.upper()}\n")
            file.write(f"Issue: {risky_services[service]}\n")

print("DEBUG: Nmap scan finished")
print("scan completed succesfully.")
print("Report saved at:", report_file)
