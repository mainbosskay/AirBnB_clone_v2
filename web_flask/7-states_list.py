#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
"""Flask application instance is established"""
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """State list page displaying HTML page"""
    sorted_states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_flask(exc):
    """Flask context end listener"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
