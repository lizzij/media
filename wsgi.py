from media import app
import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
