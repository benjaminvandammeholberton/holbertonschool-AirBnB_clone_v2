#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """ Returns a template that lists all State present in DBStorage. """
    return render_template('7-states_list.html',
                           list_s=storage.all(State).values())


@app.teardown_appcontext
def tear_down(self):
    """ Method that reloves the current SQLAlchemy Session. """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
