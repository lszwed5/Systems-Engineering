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

        avg1 = 0
        avg2 = 0
        avg3 = 0
        avg4 = 0
        avg5 = 0

        aggregated_data = False

        counter = len(list(data.keys()))
        for timestamp in list(data.keys()):
            for record in data[timestamp]:
                # pollutionData204060.csv
                try:
                    avg1 += float(data[timestamp][record]["ozone"])
                    avg2 += float(data[timestamp][record]["particullate_matter"])
                    avg3 += float(data[timestamp][record]["carbon_monoxide"])
                    avg4 += float(data[timestamp][record]["sulfure_dioxide"])
                    avg5 += float(data[timestamp][record]["nitrogen_dioxide"])

                    aggregated_data = {
                        "ozone": avg1 / counter,
                        "particullate_matter": avg2 / counter,
                        "carbon_monoxide": avg3 / counter,
                        "sulfure_dioxide": avg4 / counter,
                        "nitrogen_dioxide": avg5 / counter,
                    }
                except KeyError:
                    pass

                # trafficMetaData.csv
                try:
                    avg1 += float(data[timestamp][record]["DURATION_IN_SEC"])
                    avg2 += float(data[timestamp][record]["NDT_IN_KMH"])
                    avg3 += float(data[timestamp][record]["DISTANCE_IN_METERS"])

                    aggregated_data = {
                        "DURATION_IN_SEC": avg1 / counter,
                        "NDT_IN_KMH": avg2 / counter,
                        "DISTANCE_IN_METERS": avg3 / counter,
                    }
                except KeyError:
                    pass

                # aarhus_parking.csv
                try:
                    avg1 += float(data[timestamp][record]["vehiclecount"])
                    avg2 += float(data[timestamp][record]["totalspaces"])

                    aggregated_data = {
                        "vehiclecount": avg1 / counter,
                        "totalspaces": avg2 / counter,
                    }
                except KeyError:
                    pass

                # aarhus_libraryEvents.csv
                try:
                    avg1 += float(data[timestamp][record]["price"])

                    aggregated_data = {
                        "price": avg1 / counter
                    }
                except KeyError:
                    pass

        if aggregated_data:
            return jsonify(aggregated_data)

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
