import socket
target_host = "0.0.0.0"
target_port = 9998

def tcpClient(message):
    #create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connet the client 
    client.connect((target_host, target_port))

    #send some data
    # client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.send(message)

    response = client.recv(4096)

    print(response.decode())
    client.close()

if __name__ == '__main__':
    tcpClient(b"message test")