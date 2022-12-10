import paho.mqtt.client as mqtt
import time
import json
import requests


post_url = "http://localhost:5000/fileupload/"
topic = "A very distinctive, creative and most importantly unique mqtt topic"
broker = "test.mosquitto.org"
port = 1883

client = mqtt.Client("Middleman")
client.connect(broker, port)


def on_message(client, userdata, message):
    global post_url
    payload = message.payload.decode("utf-8").split("$")[0]
    id_ = message.payload.decode("utf-8").split("$")[1]
    print(payload)
    print(id_)
    endpoint = post_url + id_

    to_server = requests.post(endpoint, json=json.dumps(payload))
    print(to_server.text)


def main():
    client.loop_start()
    client.subscribe(topic)
    client.on_message = on_message
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
