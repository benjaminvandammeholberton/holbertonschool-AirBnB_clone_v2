#!/usr/bin/python3
"""
Module that starts a Flask web application
"""


from flask import Flask, render_template


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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    This function takes an integer 'n' as a parameter
    and returns a string indicating that 'n' is a number.

    Parameters:
    n (int): The integer input provided in the URL.

    Returns:
    str: A message stating that the input 'n' is a number.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Renders an HTML template displaying a given number.

    This route takes an integer `n` as a parameter from the URL path
    and renders the '5-number.html' template, displaying the provided number.

    Parameters:
    n (int): The number to be displayed in the template.

    Returns:
    str: Rendered HTML content containing the provided number.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
