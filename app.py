from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def index():
    logging.info('Return Home Page')
    return "Index!"

@app.route("/hello")
def hello():
    logging.info('Log Hellog Word')
    return "Hello World!"

@app.route("/members")
def members():
    logging.info('Return Members')
    return "Members"

if __name__ == "__main__":
    logging.basicConfig(filename='/var/log/app.log', level=logging.INFO)
    logging.info('Start App')
    app.run(host='0.0.0.0', port=5000)
