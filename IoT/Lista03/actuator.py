import requests
from flask import Flask, redirect, url_for, request
from template import App, ThreadWithException
from time import sleep
from requests import post
import json


app = Flask(__name__)
GENERATOR_NAME = "Radiator"
PORT = 8002
DEFAULT_TARGET = 'http://127.0.0.1:5003/upload/'
SERVER_NAME = f'{GENERATOR_NAME}:{PORT}'
REGISTER_INFO = {"Generator name": GENERATOR_NAME, "Configuration URL": f'http://127.0.0.1:{PORT}/configuration/',
                 "Type": "actuator"}
REGISTER_URL = 'http://127.0.0.1:5000/register/'
RUNNING = False
ROOM_TEMPERATURE = 25


def heat():
    global ROOM_TEMPERATURE
    while True:
        ROOM_TEMPERATURE += actuator.settings["power"] * 0.0001
        ROOM_TEMPERATURE = round(ROOM_TEMPERATURE, 2)
        sleep(6)


def cool():
    global ROOM_TEMPERATURE
    while True:
        if ROOM_TEMPERATURE >= -10:
            ROOM_TEMPERATURE -= 0.5
            ROOM_TEMPERATURE = round(ROOM_TEMPERATURE, 2)
            sleep(6)


def get_temperature():
    while True:
        # data = {"configuration": actuator.settings, "temperature": ROOM_TEMPERATURE}
        data = {"temperature": ROOM_TEMPERATURE}
        actuator.send_data(data)
        # endpoint = actuator.settings["target"]
        # to_server = requests.post(endpoint, json=json.dumps(data))
        # print(to_server.text)
        sleep(actuator.settings['frequency'])


t1 = ThreadWithException('Thread 1', heat)
t2 = ThreadWithException('Thread 2', get_temperature)
t3 = ThreadWithException('Thread 3', cool)


@app.route('/')
def index():
    return redirect(url_for('configure'))


@app.route('/configuration/', methods=['POST'])
def configure():
    global RUNNING, t1
    if request.method == 'POST':
        configuration = json.loads(request.json)
        actuator.configure(configuration)

        if configuration["is_active"]:
            if RUNNING:
                t1.raise_exception()
                t1.join()
            t1 = ThreadWithException('Thread 1', heat)
            t1.start()
            RUNNING = True
            print("\033[92m {}\033[00m".format(f"Actuator running at {configuration['power']} W"))
            # print(f"Actuator running at {configuration['power']} W")
        else:
            if RUNNING:
                t1.raise_exception()
                t1.join()
            print("\033[91m {}\033[00m".format("Actuator not running"))
            # print("Actuator not running")

    return "Configuration successful"


actuator = App()

try:
    actuator.settings['frequency']
except KeyError:
    actuator.settings = {
            "App_id": GENERATOR_NAME,
            "Configuration URL": 'http://127.0.0.1:8002/configure/',
            "datasource": None,
            "power": 0,
            "protocol": None,
            "target": 'http://127.0.0.1:5003/upload/',
            "MQTT_topic": None,
            "frequency": 10,
            "is_active": False,
            "type": "actuator"
        }

try:
    t2.start()
    t3.start()
except RuntimeError:
    pass

print("\033[91m {}\033[00m".format("Actuator not running"))


if __name__ == '__main__':
    post(REGISTER_URL, json=json.dumps(REGISTER_INFO))
    app.run(debug=False, port=PORT)
