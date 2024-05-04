import random
from datetime import datetime, timedelta
import time

# Define user domains and names
user_domains = ["CONTOSO", "FABRIKAM"]
user_names = ["user1", "user2", "admin", "guest", "jsmith", "jdoe", "asmith", "bjones", "mjohnson", "swhite"]

# Define computer names and domains
computer_domains = ["contoso.com", "fabrikam.com"]
computer_names = ["DC01", "SERVER01", "CLIENT01"]

# Event categories
event_categories = ["Account Management", "Logon/Logoff", "Object Access",
                    "Other System Events", "DS Replication"]

# Event types
event_types = ["Success Audit", "Failure Audit", "Information", "Warning", "Error"]

# Active Directory events
ad_events = {
    "User Logon": "User account '{user_domain}\\{user_name}' logged on to computer '{computer_domain}\\{computer_name}'.",
    "User Attribute Changes": "User attribute changes detected for account '{user_domain}\\{user_name}'.",
    "Account Lockout": "Account lockout detected for user '{user_domain}\\{user_name}' on computer '{computer_domain}\\{computer_name}'.",
    "Group Management": "Group management event detected for group '{group_name}'.",
    "Group Policy Object Changes": "Group Policy Object (GPO) changes detected: {gpo_changes}.",
    "Privileged User Activities": "Privileged user activity detected for user '{user_domain}\\{user_name}' on computer '{computer_domain}\\{computer_name}'."
}

# Probability of generating an Active Directory event (adjust as needed)
ad_event_probability = 0.2  # 20% probability

# Random timestamp generation within a specific range (adjust as needed)
start_date = datetime(2024, 4, 1)
end_date = datetime(2024, 4, 7)

def generate_random_event():
    """Generates a random Active Directory event message."""
    timestamp = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    user_domain = random.choice(user_domains)
    user_name = random.choice(user_names)
    computer_domain = random.choice(computer_domains)
    computer_name = random.choice(computer_names)
    event_category = random.choice(event_categories)
    event_type = random.choice(event_types)
    
    # Decide whether to generate an Active Directory event
    if random.random() < ad_event_probability:
        # Randomly select an Active Directory event
        ad_event_type = random.choice(list(ad_events.keys()))
        
        # Generate description based on selected event type
        if ad_event_type == "Group Policy Object Changes":
            gpo_changes = "Sample GPO changes"
            description = ad_events[ad_event_type].format(gpo_changes=gpo_changes)
        elif ad_event_type == "Group Management":
            group_name = "SampleGroup"
            description = ad_events[ad_event_type].format(group_name=group_name)
        else:
            description = ad_events[ad_event_type].format(user_domain=user_domain, user_name=user_name, computer_domain=computer_domain, computer_name=computer_name)
    else:
        # Generate a standard event
        description = f"Standard event generated for user '{user_domain}\\{user_name}' on computer '{computer_domain}\\{computer_name}'."


    event = {
         "Log Name" : "Security",
         "Source": "Active Directory",
         "Event ID": random.randint(4624,4899),
         "User":user_domain,
         "Category" : event_type,
         "Description":description
          
     }
    return event

def directory_events_loop():
    return generate_random_event()

