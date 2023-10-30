# OS-A3
Running the Server:
Compile and Run (Python):

Run the following command to make the assignment3 script executable:
<chmod +x assignment3.py>
Use the provided Makefile to create a script named assignment3:

Start the Server:

Run the server with the desired port and search pattern:
<./assignment3 -l 12345 -p "happy">
This command will start the server listening on port 12345 and searching for the pattern "happy" in received data.

Sending Data from a Client (Using Netcat):
You can use netcat (or nc) as a client to send data to the server.

Connect to the Server:
Use netcat to connect to the server.
For example, if the server is running on the same machine with IP 127.0.0.1:

nc 127.0.0.1 12345
Replace 127.0.0.1 with the actual IP address of the server if it's on a different machine.

Send Data:
Type in any text you want to send to the server and press Enter.

Close the Connection:
To close the connection, press Ctrl+C or use the appropriate command based on your operating system.

Cleaning Up:
If you want to remove the generated assignment3 script, you can use:
<make clean>
This will remove the script and leave only the Python source file.

Important Notes:
The server must be running before you try to connect with a client.
If you're running the client on a different machine, replace 127.0.0.1 with the actual IP address of the server.





