import requests
from flask import Flask, request, jsonify
from copy import deepcopy
import json


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    return "The mighty filter app"


@app.route('/filtrate/', methods=["POST"])
def filtrate():
    if request.method == 'POST':
        configuration = json.loads(request.json)

        try:
            with open(configuration['path'], "r") as f:
                data = json.load(f)

                filtered_data = deepcopy(data)
                for timestamp in data.keys():
                    for id_ in data[timestamp]:
                        for field in data[timestamp][id_]:
                            if field not in configuration['fields']:
                                filtered_data[timestamp][id_].pop(field)

        except FileNotFoundError:
            return "404 - File not found"

        if len(configuration['target']) > 0:
            print(filtered_data)
            print(type(filtered_data))
            send = requests.post(configuration['target'], json=json.dumps(filtered_data))
        return jsonify(filtered_data)

    return "How on Earth did You even get here"


if __name__ == '__main__':
    app.run(debug=True, port=5002)
