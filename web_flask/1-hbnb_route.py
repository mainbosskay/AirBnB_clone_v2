#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
"""Flask application instance is established"""
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """This is the home page message"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_page():
    """This is the HBNB page message"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
