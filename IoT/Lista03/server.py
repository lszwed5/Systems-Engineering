import sys
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, IntegerField, FileField, BooleanField
from wtforms.validators import InputRequired
import json
from subprocess import Popen

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'thisisasecretkey'
RECONFIG_PATH = "configs/reconfiguration.json"
ACTIVE_GENERATORS = {}


class ConfigureForm(FlaskForm):

    generator_id = SelectField(u'Generator ID: ', choices=[1, 2, 3, 4, 5], coerce=int)

    datasource = StringField('Source of data: ', validators=[InputRequired()])

    protocol = SelectField('Protocol: ', choices=['HTTP', 'MQTT'])

    target = StringField('Target URL: ', validators=[InputRequired()])

    mqtt_topic = StringField('MQTT Topic: ')

    frequency = IntegerField('Frequency of sending in seconds: ', default=0)

    is_active = BooleanField('Active: ')

    submit = SubmitField('Apply')


def rerun_generator_app(app_path, config_path):
    return Popen([sys.executable, app_path, config_path])


@app.route("/")
def index():
    return redirect(url_for('configure'))


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


@app.route("/configuration/", methods=['GET', 'POST'])
def configure():
    form = ConfigureForm()

    if form.validate_on_submit():
        configuration = {
            "App_id": form.generator_id.data,
            "datasource": form.datasource.data,
            "protocol": form.protocol.data,
            "target": form.target.data,
            "MQTT_topic": form.mqtt_topic.data,
            "frequency": form.frequency.data,
            "is_active": form.is_active.data
        }
        # print(configuration)

        generator_name = f'App{configuration["App_id"]}.py'

        with open(RECONFIG_PATH, "w", encoding='utf-8') as f:
            json.dump(configuration, f, indent=4)

        if configuration["is_active"]:
            if str(configuration["App_id"]) in ACTIVE_GENERATORS.keys():
                ACTIVE_GENERATORS[str(configuration["App_id"])].kill()
                ACTIVE_GENERATORS[str(configuration["App_id"])] = rerun_generator_app(generator_name, RECONFIG_PATH)
            else:
                ACTIVE_GENERATORS[str(configuration["App_id"])] = rerun_generator_app(generator_name, RECONFIG_PATH)
        else:
            if str(configuration["App_id"]) in ACTIVE_GENERATORS.keys():
                ACTIVE_GENERATORS[str(configuration["App_id"])].kill()

        return redirect(url_for('successful'))

    # print(form.errors)
    return render_template('configure.html', form=form)


@app.route('/configuration/success/')
def successful():
    return render_template('successful_configuration.html')


if __name__ == '__main__':
    app.run(debug=True)
