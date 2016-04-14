import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1792)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        data = connection.recv(200)
        print >>sys.stderr, 'received "%s"' % data
        if data:
            print >>sys.stderr, 'received data at destination - Socket B'
        else:
            print >>sys.stderr, 'no more data from', client_address
            break

    finally:
        # Clean up the connection
        connection.close()
