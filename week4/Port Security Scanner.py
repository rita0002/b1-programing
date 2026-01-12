# Exercise 2: Port Security Scanner

# Step 1: Define devices and their open ports
devices = [
    ("192.168.1.10", [22, 80, 443]),
    ("192.168.1.11", [21, 22, 80]),
    ("192.168.1.12", [23, 80, 3389])
]

# Step 2: Define risky ports
risky_ports = [21, 23, 3389]

print("Scanning network devices...")

# Step 3: Counter for total security risks
risk_count = 0

# Step 4: Check each device and its ports
for device in devices:
    ip_address = device[0]
    open_ports = device[1]

    for port in open_ports:
        if port in risky_ports:
            print(f"WARNING: {ip_address} has risky port {port} open")
            risk_count += 1

# Step 5: Print summary
print(f"Scan complete: {risk_count} security risks found")
