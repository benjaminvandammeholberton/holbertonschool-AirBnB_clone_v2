#!/usr/bin/python3
"""
Module that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Route handler for the root URL ("/").

    This function is executed when the root URL ("/") is accessed.

    Returns:
        str: A simple greeting message.
    """
    return ("Hello HBNB!")


@app.route("/HBNB", strict_slashes=False)
def message():
    """
    Route handler for the root URL ("/hbnb").

    This function is executed when the root URL ("/hbnb") is accessed.

    Returns:
        str: "HBNB".
    """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def Cmessage(text):
    """
    Route handler for "/c/<text>" URL.

    This function captures the value of the "text" parameter from the URL and
    returns a message containing the captured value.

    Args:
        text (str): The captured value from the URL.

    Returns:
        str: A message containing the captured value.
    """
    new_text = text.replace("_", " ")
    return (f"C {new_text}")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonmessage(text="is cool"):
    """
    Route handler for "/python/<text>" URL.

    This function captures the value of the "text" parameter
    from the URL and
    returns a message containing the captured value with
    underscores replaced by spaces.

    Args:
        text (str): The captured value from the URL.

    Returns:
        str: A message containing the captured value.
    """
    new_text = text.replace("_", " ")
    return f"Python {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
