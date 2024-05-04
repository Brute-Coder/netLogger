import random
from datetime import datetime

# Define IP address ranges
source_ip_range_start = "192.168.1.0/24"
dest_ip_range_start = "10.0.0.0/24"

# Define common protocols
protocols = ["TCP", "UDP", "ICMP"]

# Define common ports
ports = {"http": 80, "https": 443, "ssh": 22, "ftp": 21, "smtp": 25}

# Define alert severity levels
severities = ["low", "medium", "high"]

# Define signature categories (expanded list)
sig_categories = [
    "Trojan", "Web Application Attack", "Exploit", "Infection",
    "Brute Force", "Malware", "Phishing", "Denial of Service",
    "Command and Control", "Data Exfiltration", "Credential Theft",
    "Insider Threats", "Cryptojacking", "Social Engineering",
    "Anomaly Detection", "File Integrity Monitoring", "Application Layer Attacks",
    "IoT Threats"
]

def generate_ip_address(base_ip, subnet_size=24):
    """Generates a random IP address within a subnet range."""
    ip_parts = base_ip.split(".")
    if len(ip_parts) != 4:
        raise ValueError("Invalid IP address format")
    
    # Generate random host part within subnet range
    host_part = random.randint(0, 2**(32 - subnet_size) - 1)
    ip_parts[3] = str(host_part)
    return ".".join(ip_parts)

def generate_random_port():
    """Generates a random port number within a valid range."""
    return random.randint(1, 65535)

def generate_random_suricata_event():
    """Generates a random Suricata event in JSON format."""
    timestamp = datetime.utcnow().isoformat()
    source_ip = generate_ip_address(source_ip_range_start)
    dest_ip = generate_ip_address(dest_ip_range_start)
    protocol = random.choice(protocols)
    
    # Randomly choose between using a common port or a random one
    if random.random() < 0.7:  # 70% chance of using common port
        port = random.choice(list(ports.values()))
    else:
        port = generate_random_port()
    
    severity = random.choice(severities)
    sig_category = random.choice(sig_categories)
    signature_id = f"SID:{random.randint(1000, 9999)}"
    
    # Generate random message content
    message = f"Detected {severity} severity {sig_category} event involving {protocol} traffic from {source_ip}:{port} to {dest_ip}:{port}"
    
    return {
        "@timestamp": timestamp,
        "source": source_ip,
        "destination": dest_ip,
        "protocol": protocol,
        "sport": port,
        "dport": port,
        "msg": message,
        "signature":signature_id,
        "category":sig_category,
        "severity":severity
    }


def generate_suricata_events():
    return generate_random_suricata_event()

