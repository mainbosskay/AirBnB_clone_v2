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


@app.route("/c/<text>")
def c_page(text):
    """C page message displying by value <text>"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/<text>")
@app.route("/python", defaults={"text": "is cool"})
def python_page(text):
    """Python page displaying the value of <text>"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def number_page(n):
        """"Number page displaying n if it is integer"""
        return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Number template page displaying HTML pages for integers"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
