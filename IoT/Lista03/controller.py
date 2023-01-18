import json
from flask import Flask, request, render_template
import requests


with open("configs/controller_config.json", "r") as f:
    settings = json.load(f)

ROOM_TEMPERATURE = settings["ROOM_TEMPERATURE"]
TOP_LIMIT = settings["TOP_LIMIT"]
BOTTOM_LIMIT = settings["BOTTOM_LIMIT"]
ACTUATOR_CONFIGURATION_URL = 'http://127.0.0.1:8002/configuration/'
PATH = "server_files/src-Radiator.json"
PORT = 5003
app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload_measurement():
    global ROOM_TEMPERATURE, TOP_LIMIT, BOTTOM_LIMIT, ACTUATOR_CONFIGURATION_URL
    if request.method == 'POST':
        data = json.loads(request.json)

        configuration = data['configuration']
        ROOM_TEMPERATURE = data["temperature"]

        print(ROOM_TEMPERATURE, end=' ')

        if ROOM_TEMPERATURE > TOP_LIMIT:
            print("\033[91m {}\033[00m".format("Too hot"))
            configuration['is_active'] = False
        elif ROOM_TEMPERATURE < BOTTOM_LIMIT:
            print("\033[91m {}\033[00m".format("Too cold"))
            configuration['is_active'] = True
        else:
            print("\033[92m {}\033[00m".format("OK"))

        if configuration['power'] <= 0:
            configuration['is_active'] = False

        update = requests.post(ACTUATOR_CONFIGURATION_URL, json=json.dumps(configuration))
        print(update.text)

        return "Data sent successfully"


@app.get('/get_temperature/')
def get_temperature():
    if ROOM_TEMPERATURE > TOP_LIMIT:
        answer = "Too hot"
    elif ROOM_TEMPERATURE < BOTTOM_LIMIT:
        answer = "Too cold"
    else:
        answer = "OK"
    return render_template('controller.html', ROOM_TEMPERATURE=ROOM_TEMPERATURE, answer=answer)


if __name__ == '__main__':
    app.run(debug=False, port=PORT)
