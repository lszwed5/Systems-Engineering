from template import App
from time import sleep
import sys


app = App()
if len(sys.argv) == 1:
    print("No config dictionary given")
    sys.exit(1)
configuration = sys.argv[1]
app.configure(configuration)
# app.configure("configs/App_1_Config.json")
frequency = app.settings['frequency']

while True:
    data = app.get_data()
    app.send_data(data)
    sleep(frequency)
