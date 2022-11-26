from template import App
from time import sleep


app = App()
app.configure("configs/App_2_Config.json")
frequency = app.settings['frequency']

while True:
    data = app.get_data()
    app.send_data(data)
    sleep(frequency)
