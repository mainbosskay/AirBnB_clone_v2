#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models import storage


app = Flask(__name__)
"""Flask application instance is established"""
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb():
    """HBNB filters page displaying HTML page with details"""
    sorted_states = sorted(storage.all(State).values(), key=lambda k: k.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda k: k.name)
    places = sorted(storage.all(Place).values(), key=lambda k: k.name)
    for state in sorted_states:
        state.cities.sort(key=lambda k: k.name)
    for place in places:
        place.description = Markup(place.description)
    return render_template("100-hbnb.html", states=sorted_states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_flask(exc):
    """Flask context end listener"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
