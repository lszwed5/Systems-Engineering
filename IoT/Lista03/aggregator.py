from flask import Flask, request, jsonify
import json
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    return "Hello, world"


@app.route('/configure/<src>', methods=["POST"])
def configure(src):
    if request.method == 'POST':
        configuration = json.loads(request.json)

        path = f"server_files/src-{src}.json"
        try:
            with open(path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return "404 - File not found"

        if configuration["Time span"] != "All":
            now = datetime.now()

            for key in list(data.keys()):
                if datetime.strptime(key, "%Y-%m-%d %H:%M:%S") \
                        < now - timedelta(seconds=int(configuration["Time span"])):
                    data.pop(key)

    return jsonify(data)


@app.route("/fileupload/<src>", methods=["POST"])
def file_upload(src):
    if request.method == 'POST':
        data = json.loads(request.json)
        if type(data) != dict:
            data = eval(data)

        save_path = f"server_files/src-{src}.json"

        try:
            with open(save_path, "r") as f:
                r = json.load(f)
                data.update(r)
        except FileNotFoundError:
            pass

        with open(save_path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return "Upload successful"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
