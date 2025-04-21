import socket
from datetime import datetime


# Check if the target IP address is valid
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False


# Check if the target port number is valid
def is_valid_port(port):
    return 1 <= port <= 65535


# Check if a port is open
def is_open_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False


# Print open ports
def print_open_ports(ip):
