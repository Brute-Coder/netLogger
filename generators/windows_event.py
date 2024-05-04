import random
import string

# Function to generate a random string
def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate a valid description message
def generate_description():
    messages = [
        "Application started successfully.",
        "Disk space is running low. Please free up disk space.",
        "An error occurred while processing the request. Error code: 0x80070005 (Access Denied).",
        "A new user account was created.",
        "Service stopped unexpectedly. Please check the service status.",
        "Network connection established.",
        "Critical system update installed successfully.",
        "Invalid username or password entered during logon attempt.",
        "Database connection established.",
        "File not found: C:\\Windows\\System32\\file.txt",
        "System reboot initiated.",
        "Backup operation completed successfully.",
        "Printer error: Paper jam detected.",
        "Disk drive failure detected.",
        "Memory usage exceeded threshold. Consider upgrading RAM.",
        "Network connectivity lost. Reconnecting...",
        "Security audit trail cleared.",
        "Software update available. Please install the latest updates.",
        "System shutdown initiated.",
        "Unauthorized access detected. Alerting security team."
    ]
    return random.choice(messages)

# Function to generate random events
def generate_windows_events():  
    event_id = random.randint(1, 1000)
    level = random.choice(["Information", "Warning", "Error", "Audit Success", "Audit Failure"])
    source = random.choice(["Application", "System", "Security", "CustomCategory"])
    description = generate_description()
    event = {
        "Source": source,
        "Event ID": event_id,
        "Level": level,
        "Description": description
    }
    return event
