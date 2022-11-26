import paho.mqtt.client as mqtt
import time
import json
import requests


post_url = "http://localhost:5000/battery_percentage/upload/"
broker = "test.mosquitto.org"
port = 1883

client = mqtt.Client("Messenger")
client.connect(broker, port)


def on_message(client, userdata, message):
    info = {
        message.payload.decode("utf-8").split("$")[0]: message.payload.decode("utf-8").split("$")[1]
    }
    print(info)
    to_server = requests.post(post_url, json=json.dumps(info))
    print(to_server.text)


client.loop_start()
client.subscribe("battery/percentage")
client.on_message = on_message
while True:
    time.sleep(1)
