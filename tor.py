import socks
import socket
import requests
import time

def connect_to_tor():
	socks.setdefaultproxy(proxy_type=socks.SOCKS5, addr="127.0.0.1", port=9050)
	socket.socket = socks.socksocket


def refresh_ip():

	socks.setdefaultproxy()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#Connect through controlport 9051 to send commands
	s.connect(("127.0.0.1", 9051))
	s.send(("AUTHENTICATE\r\n").encode())
	s.send(("SIGNAL NEWNYM\r\n").encode())
	s.close()
	connect_to_tor()


if __name__ == '__main__':

	'''
	Example usage
	'''

	connect_to_tor()
	print ("Connected to Tor with IP - " + requests.get("http://icanhazip.com").text)

	#Wait a bit before refreshing the IP (beware of rate limiting by tor if this is done too frequently)
	time.sleep(5)

	refresh_ip()
	print ("Refreshed IP. New IP is - " + requests.get("http://icanhazip.com").text)
