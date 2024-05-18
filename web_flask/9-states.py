#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)
"""Flask application instance is established"""
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states_and_id(id=None):
    """State page displaying HTML page of state id"""
    sorted_states = sorted(storage.all(State).values(), key=lambda k: k.name)
    case = 404
    if id is not None:
        exptd = list(filter(lambda k: k.id == id, sorted_states))
        if len(exptd) > 0:
            state = exptd[0]
            state.cities.sort(key=lambda k: k.name)
            case = 2
            return render_template("9-states.html", state=state, case=case)
    else:
        states = sorted_states
        for state in states:
            state.cities.sort(key=lambda k: k.name)
        states.sort(key=lambda k: k.name)
        case = 1
        return render_template("9-states.html", states=states, case=case)
    return render_template("9-states.html", case=case)


@app.teardown_appcontext
def teardown_flask(exc):
    """Flask context end listener"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
