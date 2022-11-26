import csv
import json
import requests
import paho.mqtt.client as mqtt


class App:
    """A template for IoT L3 application"""
    def __init__(self):
        self.settings = None

    def configure(self, filename):
        with open(filename, "r") as f:
            self.settings = json.load(f)

    def get_data(self):
        source = self.settings["datasource"]
        data = {}

        with open(source, encoding='utf-8') as f:
            reader = csv.reader(f)
            key_column = next(reader)[0]

        with open(source, encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                key = row[key_column]
                data[key] = row

        return data

    def send_data(self, data):
        match self.settings["protocol"]:
            case "HTTP":
                endpoint = self.settings["target"] + str(self.settings["App_id"])

                to_server = requests.post(endpoint, json=json.dumps(data))
                print(to_server.text)

            case "MQTT":
                broker = self.settings["target"]
                topic = self.settings["MQTT_topic"]
                client = mqtt.Client(f"App_{self.settings['App_id']}")

                client.connect(broker, 1883)
                client.publish(topic, str(data) + f"${self.settings['App_id']}")
                client.disconnect()
