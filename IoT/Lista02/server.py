from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    return "Hello world!"


@app.route("/battery_percentage/upload/", methods=["POST"])
def upload_battery_data():
    if request.method == 'POST':
        data = json.loads(request.json)
        print(type(data))

        try:
            with open("battery_status.json", "r") as f:
                r = json.load(f)
                data.update(r)
        except FileNotFoundError:
            pass

        with open("battery_status.json", "w") as f:
            json.dump(data, f, indent=4)

        return "Upload successful"


@app.route("/battery_percentage/get/", methods=["get"])
def get_battery_data():
    try:
        with open("battery_status.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return "404 - File not found"
    return jsonify(data)


if __name__ == "__main__":
    app.run()
