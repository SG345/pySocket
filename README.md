# pySocket

A program in python that reads arbitrary input from a socket and forwards it to another socket.

## Instructions for running the source code:


send_data.py : It has some message, which will be sent to *Socket A*

A.py: This would initiate *Socket A*, receive data which is sent here from from send_data.py and forwards it to destination, i.e. *Socket B*

B.py: This will receive the data which is sent from *Socket A*.


For running the source-code, the files need to be executed in the following order:

1) execute B.py in one terminal tab

2) execute A.py in another terminal tab

3) execute send_data.py in another tab.
