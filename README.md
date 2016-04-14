# pySocket

A program in python that reads arbitrary input from a socket and forwards it to another socket.

## Instructions for running the source code:


send_data.py : It has some message, which will be sent to *Socket A*

A.py: This would initiate *Socket A*, receive data which is sent here from from send_data.py and forwards it to destination, i.e. *Socket B*

B.py: This will receive the data which is sent from *Socket A*.


For running the source-code, the files need to be executed in the following order:

1) run *B.py* in one terminal tab

2) run *A.py* in another terminal tab

3) run *send_data.py* in another terminal tab.

## Notes:
The following assumptions/design decisions were taken to complete the task. 

1) The message which is being sent to *Socket A* and forwarded to *Socket B* is currently hardcoded in *send_data.py*. 

2) The program will not work and will throw an exception error if the port numbers are currently being used by another application.

Port numbers of *Socket A* and *Socket B* are also currently *hardcoded*.
