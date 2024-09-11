import socket

def scan_port(ip, port):
    """ Function to scan a specific port on an IP address """
    # Create a socket object
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Set timeout of 1 second

    # Try to connect to the port
    result = scanner.connect_ex((ip, port))
    
    # Check if the port is open (result 0 means open)
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    
    scanner.close()

def scan_ports(ip, start_port, end_port):
    """ Scan a range of ports on a given IP address """
    print(f"Scanning {ip} for open ports between {start_port} and {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# User input for target IP address and port range
target_ip = input("Enter the IP address to scan: ")
start_port = int(input("Enter the start port number: "))
end_port = int(input("Enter the end port number: "))

# Call the port scanning function
scan_ports(target_ip, start_port, end_port)
