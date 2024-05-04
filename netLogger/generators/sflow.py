import random
import socket
import struct
import time

def generate_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def generate_random_mac():
    return ':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(6)])

def generate_sflow_event():
    # Generate synthetic data for each field
    agent_address = "192.168.1.1"
    sub_agent_id = 1
    sample_type = "flow_sample"
    sequence_number = random.randint(1, 1000)
    source_ip = generate_random_ip()
    source_port = random.randint(1024, 65535)
    source_mac = generate_random_mac()
    destination_ip = generate_random_ip()
    destination_port = random.randint(1024, 65535)
    destination_mac = generate_random_mac()
    protocol = "TCP"
    type_of_service = random.randint(0, 255)
    ip_protocol_version = 4
    tcp_flags = "SYN"
    packet_size = random.randint(64, 1500)
    sampling_rate = 1000
    timestamp = int(time.time())
    input_interface = 1
    output_interface = 2
    vlan_id = 100

    # Construct sFlow event dictionary
    sflow_event = {
        "agent_address": agent_address,
        "sub_agent_id": sub_agent_id,
        "sample_type": sample_type,
        "sequence_number": sequence_number,
        "source_ip": source_ip,
        "source_port": source_port,
        "source_mac": source_mac,
        "destination_ip": destination_ip,
        "destination_port": destination_port,
        "destination_mac": destination_mac,
        "protocol": protocol,
        "type_of_service": type_of_service,
        "ip_protocol_version": ip_protocol_version,
        "tcp_flags": tcp_flags,
        "packet_size": packet_size,
        "sampling_rate": sampling_rate,
        "timestamp": timestamp,
        "input_interface": input_interface,
        "output_interface": output_interface,
        "vlan_id": vlan_id,
        
    }

    return sflow_event


def generate_sFlow():
   return generate_sflow_event()
