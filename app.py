import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('website.html', variable='RAPH SMEELS GAY')

app.run(debug=True)
