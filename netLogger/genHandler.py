from generators.process import process_event_generator
from generators.SQL_server_security import sql_event_generator 
from generators.windows_event import generate_windows_events
from generators.suricata_events import generate_suricata_events
from generators.active_directory import directory_events_loop
from generators.sflow import generate_sFlow

eventMapper = {
    "system-process" : process_event_generator,
    "sql-server-events" : sql_event_generator,
    "windows-generator-event" : generate_windows_events,
    "suricata-events" : generate_suricata_events,
    "directory-events" : directory_events_loop,
    "sFlow-events" : generate_sFlow
}

def eventGenerator(eventType):
    data = eventMapper[eventType]()
    return data