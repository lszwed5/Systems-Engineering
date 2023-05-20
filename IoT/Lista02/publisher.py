import time
import paho.mqtt.client as mqtt
from psutil import sensors_battery
from datetime import datetime


broker = "test.mosquitto.org"
port = 1883
percentage = sensors_battery().percent

client = mqtt.Client("Battery_sensor")


while True:
    battery = sensors_battery().percent

    if abs(percentage - battery) >= 1:
        client.connect(broker, port)
        timestamp = datetime.now()
        timestamp = str(timestamp.replace(microsecond=0))
        percentage = battery
        client.publish("battery/percentage", timestamp + "$" + str(percentage))
        print("battery/percentage", timestamp + "$" + str(percentage))
        client.disconnect()
    time.sleep(10)
