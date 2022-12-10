import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired
import json
import threading
from middleman import main


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'thisisasecretkey'
ACTIVE_GENERATORS = {}
CONFIGURATIONS = {}
CONNECTED_GENERATORS = {}


class ConfigureForm(FlaskForm):

    generator_id = SelectField(u'Generator ID: ', choices=CONNECTED_GENERATORS.keys())

    datasource = StringField('Source of data: ', validators=[InputRequired()])

    protocol = SelectField('Protocol: ', choices=['HTTP', 'MQTT'])

    target = StringField('Target URL: ', validators=[InputRequired()])

    mqtt_topic = StringField('MQTT Topic: ')

    frequency = IntegerField('Frequency of sending in seconds: ', default=0)

    is_active = BooleanField('Active: ')

    submit = SubmitField('Apply')


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home/")
def home():
    return render_template('index.html',
                           data={"active_generators": ACTIVE_GENERATORS, "configurations": CONFIGURATIONS})


@app.route('/register/', methods=["POST"])
def register():
    if request.method == 'POST':
        data = json.loads(request.json)
        CONNECTED_GENERATORS[data["Generator name"]] = data["Configuration URL"]
        CONFIGURATIONS[data["Generator name"]] = {
            "App_id": data["Generator name"],
            "Configuration URL": data["Configuration URL"],
            "datasource": None,
            "protocol": None,
            "target": None,
            "MQTT_topic": None,
            "frequency": None,
            "is_active": False
        }
        print(CONNECTED_GENERATORS)

    return "Connected successfully"


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


@app.route("/configuration/<id_>", methods=['GET', 'POST'])
def configure(id_):
    form = ConfigureForm()

    if id_ != 'all':
        form.generator_id.choices = [id_]
        print(CONFIGURATIONS)
        if CONFIGURATIONS[str(id_)]["datasource"]:
            form.datasource.default = CONFIGURATIONS[str(id_)]["datasource"]
        if CONFIGURATIONS[str(id_)]["protocol"]:
            form.protocol.default = CONFIGURATIONS[str(id_)]["protocol"]
        if CONFIGURATIONS[str(id_)]["target"]:
            form.target.default = CONFIGURATIONS[str(id_)]["target"]
        if CONFIGURATIONS[str(id_)]["MQTT_topic"]:
            form.mqtt_topic.default = CONFIGURATIONS[str(id_)]["MQTT_topic"]
        if CONFIGURATIONS[str(id_)]["frequency"]:
            form.frequency.default = CONFIGURATIONS[str(id_)]["frequency"]
        form.is_active.default = CONFIGURATIONS[str(id_)]["is_active"]

    if form.validate_on_submit():
        configuration = {
            "App_id": form.generator_id.data,
            "Configuration URL": CONNECTED_GENERATORS['App1'],
            "datasource": form.datasource.data,
            "protocol": form.protocol.data,
            "target": form.target.data,
            "MQTT_topic": form.mqtt_topic.data,
            "frequency": form.frequency.data,
            "is_active": form.is_active.data
        }

        send = requests.post(configuration["Configuration URL"], json=json.dumps(configuration))
        print(send.text)
        # print(configuration)

        CONFIGURATIONS[str(configuration["App_id"])] = configuration

        # return redirect(url_for('home'))
        return redirect(url_for('successful'))

    form.process()
    # print(form.errors)
    return render_template('configure.html', form=form)


@app.route('/configuration/success/')
def successful():
    return render_template('successful_configuration.html')


if __name__ == '__main__':
    t1 = threading.Thread(target=main, daemon=True)
    t1.start()
    app.run(debug=True)
