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
  return("Hello HBNB!")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
