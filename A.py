import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is some arbitrary port number and address for this socket
server_address = ('localhost', 5498)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

destination = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is another arbitrary socket where we are going to send whatever
# data we receive on this socket
destination_address = ('localhost', 1792)
# establish a connection with the destination socket
destination.connect(destination_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        data = connection.recv(200)
        print >>sys.stderr, 'received the following data at socket A:  "%s"' % data
        if data:
            print >>sys.stderr, 'sending data to socket B: ....'
            destination.sendall(data)  # Send whatever is received to socket B

    finally:
        # Clean up the connection
        connection.close()
