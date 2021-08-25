"""Code for a flask API to Create, Read, Update, Delete users"""
import os
import sys
import psutil
from flask import jsonify, request, Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Welcome to flask CPU api!"


@app.route("/demo")
def add_user():
    """Function to return the host's cpu"""
    psutil.PROCFS_PATH = '/hostfs/proc'
    cpu = psutil.cpu_percent()
    if cpu < 60:
        print("Process completed", flush=True)
        return jsonify({}), 202
    else:
        print("Cannot perform request, CPU is too high on the host", flush=True)
        return jsonify({}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
