from flask import Flask, request, jsonify, render_template
from numpy import DataSource
from scripts import c_mail
import time

app = Flask("app")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET'])
def booking():
    c_mail.email("switch.mc.astro@gmail.com","test")

@app.route('/api', methods=['POST'])
def api():
    return "api called with data: " + request.form['data'] + " error: decaprated/removed/not implemented"

@app.route('/api/booking', methods=['POST'])
def api_booking():
    return "api called with data: " + request.form['data'] + " error: decaprated/removed/not implemented"

app.run("0.0.0.0", debug=True)
