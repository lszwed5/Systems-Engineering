from flask import Flask, request, jsonify
import json


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/fileupload/<src>", methods=["POST"])
def file_upload(src):
    if request.method == 'POST':
        data = json.loads(request.json)
        if type(data) != dict:
            data = eval(data)

        save_path = f"server_files/src-{src}.json"
        with open(save_path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        return "Upload successful"


@app.route("/getfile/<file_nr>", methods=["get"])
def getfile(file_nr):
    path = f"server_files/src-{file_nr}.json"
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return "404 - File not found"
    return jsonify(data)


if __name__ == '__main__':
    app.run()
