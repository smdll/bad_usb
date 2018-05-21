# Basically this script is to create a TCP server, receive messages and print them out.

import socket, threading

ip_addr = '127.0.0.1'
listen_port = 1234

def post(sock, addr):
	try:
		rawdata = sock.recv(2048)
		print '%s:%s sends '%addr + rawdata
	except:
		pass
	finally:
		sock.close()

if __name__ == '__main__':
	recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	recv.bind((ip_addr, listen_port))
	recv.listen(5)
	while True:
		sock, addr = recv.accept()
		t = threading.Thread(target = post, args=(sock, addr))
		t.start()
