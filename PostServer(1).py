import flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def message():
    if request.method == 'POST':
        app.logger.info('Request received.')
        app.logger.info('Url: %s', request.url)
        app.logger.info('Data: %s', request.data)
        app.logger.info('Is JSON: %s', request.is_json)
    else:
        app.logger.info('GET request received.')
    return 'OK\n'

if __name__ == '__main__':
    app.run(host='169.254.10.102', port=8080, debug=1)

