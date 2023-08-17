#!/usr/bin/python3
"""A simple Flask application displaying 'states list' at the root."""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def close(e):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
