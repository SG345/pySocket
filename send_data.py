import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server of Socket A is listening
server_address = ('localhost', 5498)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    # Send data
    message = 'I am excited and eagerly looking to work on YAPDNS project'
    print >>sys.stderr, 'Sending the following message to socket A...."%s"' % message
    sock.sendall(message)  # Send the message to Socket A

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
