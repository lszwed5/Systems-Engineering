import csv
import ctypes
import threading
import json
import requests
import paho.mqtt.client as mqtt


class App:
    """A template for IoT L3 application"""

    def __init__(self):
        self.settings = None

    def configure_from_file(self, filename):
        with open(filename, "r") as f:
            self.settings = json.load(f)

    def configure(self, json_data):
        self.settings = json_data

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


class ThreadWithException(threading.Thread):
    def __init__(self, name, function, args=None):
        threading.Thread.__init__(self)
        self.name = name
        self.function = function
        self.args = args

    def run(self):

        # target function of the thread class
        try:
            if self.args:
                self.function(self.args)
            else:
                self.function()
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id_, thread in threading._active.items():
            if thread is self:
                return id_

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
