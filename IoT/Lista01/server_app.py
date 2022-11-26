from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def index():
    """The server's index page"""
    return '<h1>Index Page</h1>'


@app.route('/fileupload/', methods=['GET', 'POST'])
def upload_file():
    """Allows You to upload a file to the server via HTTP POST"""
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(f'server_memory/{filename}')
        return 'File uploaded successfully'
    return redirect(url_for('index'))


@app.route('/getfile/')
def get_file():
    """Allows You to access a file on the server via HTTP GET"""
    filename = request.args['filename']
    try:
        with open(f"server_memory/{filename}", 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "Error 404 - Sorry, there's no such file or directory on the server"
    if 'line' in request.args.keys() and request.args['line'] is not None:
        content = content.splitlines()
        line = int(request.args['line'])
        if 0 < line <= len(content):
            return content[line - 1]
        else:
            return "Error 404 - There is no such line in this file"
    else:
        return content


if __name__ == "__main__":
    app.run()
