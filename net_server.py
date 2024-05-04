
#Below is the fully updated server.py file that implements a more complex thread management system. 
#API endpoints to dynamically update these configurations. This approach allows for granular control 
#over each thread, enabling changes to their respective network settings (IP, port, protocol) and the 
#delay between event generations.

#Explanation and Features
#Thread Management and Configuration:

#Each thread's configuration is stored in a dictionary (thread_configs), keyed by a unique thread_id. 
#This configuration includes the network logger instance and the delay for event generation.
#A global lock (thread_lock) is used to synchronize access to the thread_configs dictionary to prevent race conditions.
#Dynamic Configuration Endpoints:

#/start-continuous-events: Starts a new thread for continuous event generation with the specified network 
#settings and delay.
#/update-thread-config: Allows updating the configuration (IP, port, protocol, delay) of an existing thread
#based on its thread_id.

#Safety and Robustness:

#The use of a lock ensures that changes to thread configurations are thread-safe, preventing multiple 
#threads from modifying the configuration simultaneously.
#The system can dynamically

from flask import Flask, jsonify, request
from flask_cors import CORS
import socket
import json
import time
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor
from genHandler import eventGenerator

app = Flask(__name__)
CORS(app)
print(socket.gethostbyname(socket.gethostname()))
DEFAULT_NETWORK_CONFIG = {
    "IP": "192.168.31.173",
    "PORT": 12345,
    "PROTOCOL": "TCP",  # Default protocol
    "EVENTTYPE" : "/windows-generator-event"
}

# Executor for thread management not used in this advanced example
# executor = ThreadPoolExecutor(max_workers=8)

class NetworkLogger:
    def __init__(self, ip, port, protocol, eventType):
        self.ip = ip
        self.port = port
        self.protocol = protocol.upper()
        self.eventType = eventType[1:]

    def send_over_network(self, data):
        message = json.dumps(data).encode('utf-8')
        if self.protocol == "TCP":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.ip, self.port))
                if message:
                    sock.sendall(message)
        elif self.protocol == "UDP":
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.sendto(message, (self.ip, self.port))

# Dictionary to store thread configurations and references
thread_configs = {}
thread_lock = Lock()
thread_counter = 0

def process_event_generator(eventType):
    data = eventGenerator(eventType)
    return data


def continuous_event_sender(thread_id):
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # sock.connect()
    while True:
        if thread_id not in thread_configs:
            break
        config = thread_configs[thread_id]
        logger = config['logger']
        event = process_event_generator(logger.eventType)  # Assuming this function generates an event
        config['logger'].send_over_network(event)
        time.sleep(config['delay'])  # Pause for the configured delay

@app.route('/start-continuous-events', methods=['POST'])
def start_continuous_events():
    global thread_counter
    data = request.json
    delay = float(data.get('delay', 1.0))  # Default delay is 1 second
    delay = max(0.5, min(delay, 3.0))  # Constrain delay between 0.5 and 3 seconds
    ip = data.get('ip', DEFAULT_NETWORK_CONFIG['IP'])
    port = int(data.get('port', DEFAULT_NETWORK_CONFIG['PORT']))
    protocol = data.get('protocol', DEFAULT_NETWORK_CONFIG['PROTOCOL'])
    eventType = data.get('eventType',DEFAULT_NETWORK_CONFIG['EVENTTYPE'])

    logger = NetworkLogger(ip, port, protocol,eventType)
    thread_id = thread_counter
    
    with thread_lock:
        thread_configs[thread_id] = {'delay': delay, 'logger': logger}
        thread = Thread(target=continuous_event_sender, args=(thread_id,))
        thread.start()
        thread_counter += 1

    return jsonify({'message': 'Continuous event generation started', 'thread_id': thread_id})

@app.route('/update-thread-config', methods=['POST'])
def update_thread_config():
    data = request.json
    thread_id = data['thread_id']
    new_delay = float(data.get('delay', 1.0))
    new_ip = data.get('ip', DEFAULT_NETWORK_CONFIG['IP'])
    new_port = int(data.get('port', DEFAULT_NETWORK_CONFIG['PORT']))
    new_protocol = data.get('protocol', DEFAULT_NETWORK_CONFIG['PROTOCOL'])
    new_eventType = data.get('eventType',DEFAULT_NETWORK_CONFIG['EVENTTYPE'])

    new_logger = NetworkLogger(new_ip, new_port, new_protocol,new_eventType)
    
    with thread_lock:
        if thread_id in thread_configs:
            thread_configs[thread_id]['delay'] = max(0.5, min(new_delay, 3.0))
            thread_configs[thread_id]['logger'] = new_logger
            return jsonify({'message': 'Thread configuration updated', 'thread_id': thread_id})
        else:
            return jsonify({'error': 'Invalid thread ID'}), 404
        
@app.route('/stop-event-generation', methods=['POST'])
def stop_event_generation():
    data = request.json
    thread_id = data.get('thread_id')
    print(thread_id)
    global thread_counter
    with thread_lock:
        if thread_id in thread_configs:
            del thread_configs[thread_id]
            thread_counter -= 1 
            # return jsonify({'message': f'Event generation stopped for thread {thread_id}'})
            return jsonify({'message': 'Event generation stoppend', 'thread_id': thread_id})
        else:
            return jsonify({'error': 'Invalid thread ID'}), 404

if __name__ == "__main__":
    app.run(debug=True)
