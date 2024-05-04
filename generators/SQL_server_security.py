import random
from datetime import datetime

# Define user names
user_names = ["user1", "user2", "admin", "guest"]

# Define database names
database_names = ["Sales", "Marketing", "Finance", "HR"]

# Define server names
server_names = ["server1", "server2", "server3"]

# Define IP addresses
ip_addresses = ["192.168.1.10", "10.0.0.1", "172.16.0.50"]

# Define event categories
event_categories = {
    "Access Control": ["Login Success", "Login Failure", "Role Membership Changed"],
    "Data Modification": ["Insert", "Update", "Delete", "Schema Changed"],
    "Administrative": ["Server Config Changed", "Backup Completed", "Backup Failed"],
    "Privilege Escalation": ["Grant Permission", "Revoke Permission", "Ownership Changed"]
}

# Define DML statements (for Data Modification events)
dml_statements = {
    "Insert": "INSERT INTO dbo.Customers (Name, Email) VALUES ('New Customer', 'newcustomer@example.com')",
    "Update": "UPDATE dbo.Products SET Price = Price * 1.1 WHERE Category = 'Electronics'",
    "Delete": "DELETE FROM dbo.Orders WHERE OrderDate < '2024-01-01'"
}

def sql_event_generator():
    """Generates a random SQL Server security event."""
    timestamp = datetime.utcnow().isoformat()
    event_category = random.choice(list(event_categories.keys()))
    event_type = random.choice(event_categories[event_category])
    user_name = random.choice(user_names)
    server_name = random.choice(server_names)
    client_ip = random.choice(ip_addresses)

    # Specific details based on event type
    if event_category == "Access Control":
        if event_type == "Login Success" or event_type == "Login Failure":
            message = f"{event_type} for user '{user_name}' from IP '{client_ip}' on server '{server_name}'"
        else:
            new_role = random.choice(["db_owner", "db_datareader"])
            message = f"User '{user_name}' granted '{new_role}' role on database '{random.choice(database_names)}'"
    elif event_category == "Data Modification":
        dml_type = random.choice(list(dml_statements.keys()))
        statement = dml_statements[dml_type]
        message = f"User '{user_name}' on server '{server_name}' executed {dml_type} statement: {statement}"
    elif event_category == "Administrative":
        if event_type == "Server Config Changed":
            message = f"Server configuration changed on '{server_name}' by user '{user_name}'"
        elif event_type == "Backup Completed":
            database_name = random.choice(database_names)
            message = f"Backup of database '{database_name}' on server '{server_name}' completed successfully"
        else:
            message = f"Backup of database '{random.choice(database_names)}' on server '{server_name}' failed"
    else:
        object_type = random.choice(["table", "view"])
        object_name = f"dbo.{random.choice(['Customers', 'Orders', 'Products'])}"
        new_owner = random.choice(user_names)
        message = f"Ownership of {object_type} '{object_name}' on server '{server_name}' changed from '{user_name}' to '{new_owner}'"

    return {
        "@timestamp": timestamp,
        "User": user_name,
        "Server": server_name,
        "Client IP": client_ip,
        "Event Category": event_category,
        "Event Type": event_type,
        "Message": message
    }
