# Mitali Sanwal ms4952@drexel.edu
# CS530: DUI, Assignment [1]
from flask import Flask, render_template, send_file, request
import os
import json

app = Flask(__name__, static_folder='public', static_url_path='')

with open('data.json') as f:
    data = json.load(f)

# Handle the index (home) page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_file(os.path.join(app.root_path, 'public', 'img', 'goat2.png'))

# Handle any files that begin "public/" by loading from the course directory
@app.route('/public/<path:path>')
def base_static(path):
    return send_file(os.path.join(app.root_path, 'public', path))


# Handle any unhandled filename by loading its template
@app.route('/<name>')
def generic(name):
    params = request.args
    return render_template(name + '.html', params=params, value=data)


# Any additional handlers that go beyond simply loading a template
# (e.g., a handler that needs to pass data to a template) can be added here

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8142, debug=False)
