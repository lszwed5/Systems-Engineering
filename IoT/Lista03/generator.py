from flask import Flask, redirect, url_for, request
from template import App, ThreadWithException
from time import sleep
from requests import post
import json


app = Flask(__name__)
GENERATOR_NAME = "Traffic"
PORT = 8001
SERVER_NAME = f'{GENERATOR_NAME}:{PORT}'
REGISTER_INFO = {"Generator name": GENERATOR_NAME, "Configuration URL": f'http://127.0.0.1:{PORT}/configuration/',
                 "Type": "generator"}
REGISTER_URL = 'http://127.0.0.1:5000/register/'
RUNNING = False


def main():
    while True:
        data = generator.get_data()
        generator.send_data(data)
        sleep(generator.settings['frequency'])


t1 = ThreadWithException('Thread 1', main)


@app.route('/')
def index():
    return redirect(url_for('configure'))


@app.route('/configuration/', methods=['POST'])
def configure():
    global RUNNING, t1
    if request.method == 'POST':
        configuration = json.loads(request.json)
        generator.configure(configuration)

        if configuration["is_active"]:
            if RUNNING:
                t1.raise_exception()
                t1.join()
            t1 = ThreadWithException('Thread 1', main)
            t1.start()
            RUNNING = True
        else:
            if RUNNING:
                t1.raise_exception()
                t1.join()

    return "Configuration successful"


generator = App()

if __name__ == '__main__':
    post(REGISTER_URL, json=json.dumps(REGISTER_INFO))
    app.run(debug=True, port=PORT)

# if len(sys.argv) == 1:
#     print("No config dictionary given")
#     sys.exit(1)
# configuration = sys.argv[1]
# generator.configure(configuration)
