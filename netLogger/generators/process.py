import random
import string
import datetime

def process_event_generator():
    event_id = random.randint(1, 1000)
    provider = "example_provider"
    version = "1.0"
    level = random.choice([1, 2, 3, 4])
    task = random.randint(1, 10)
    opcode = random.randint(0, 5)
    keywords = "0x" + ''.join(random.choices(string.hexdigits, k=16))
    time_created = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    event_record_id = random.randint(1, 100000)
    process_id = random.randint(1, 1000)
    thread_id = random.randint(1, 10000)
    user = ''.join(random.choices(string.ascii_lowercase, k=5))
    process_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".exe"
    direction = random.choice(["Inbound", "Outbound"])
    initiating_process_id = random.randint(1, 1000)
    source_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    source_port = random.randint(1, 65535)
    destination_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    destination_port = random.randint(1, 65535)
    user_agent = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

    event_data = {
        "EventID": event_id,
        "Provider": provider,
        "Version": version,
        "Level": level,
        "Task": task,
        "Opcode": opcode,
        "Keywords": keywords,
        "TimeCreated": time_created,
        "EventRecordID": event_record_id,
        "ProcessID": process_id,
        "ThreadID": thread_id,
        "User": user,
        "ProcessName": process_name,
        "Direction": direction,
        "InitiatingProcessID": initiating_process_id,
        "SourceIP": source_ip,
        "SourcePort": source_port,
        "DestinationIP": destination_ip,
        "DestinationPort": destination_port,
        "UserAgent": user_agent
    }
    return event_data
