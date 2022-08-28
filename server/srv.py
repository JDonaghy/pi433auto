# Import the flask library
from flask import Flask
import json

# create the flask application object pa
app = Flask(__name__)

## Decorator making the subsequent function a route
@app.route("/", methods=["GET"])
## this functions return value is the response of the route (function name doesn't matter)
def first_route():
  f = open("codes.json",)
  codedefs = json.load(f)
  f.close()

  return codedefs, 200 ## will return text with a 200 status