import socket

def port_scan(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    
    result = client.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

port = int(input("[*] Select port to verification: "))
port_scan("0.0.0.0", port)
