# This file gives an example of sending the attack payload back to the target

from flask import Flask

app = Flask('__main__')

@app.route('/', methods = ['POST', 'GET'])
def root():
	return 'echo "you\'ve got pwned!"'

if __name__ == '__main__':
	app.run(port = 80)