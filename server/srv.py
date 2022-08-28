# Import the flask library
from flask import Flask, request
from flask_cors import CORS
import json
import shutil
import time

codesFile = "codes.json"


# create the flask application object pa
app = Flask(__name__)
CORS(app)

def read_codes():
  f = open(codesFile,)
  codedefs = json.load(f)
  f.close()
  return codedefs


@app.route("/", methods=["GET"])
def first_route():
  codedefs = read_codes()
  return codedefs, 200 

@app.route('/codes', methods=['POST'])
def update():
    content_type = request.headers.get('Content-Type')
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    codesFileParts = codesFile.split('.')
    shutil.copyfile(codesFile, 
      f"{codesFileParts[0]}-{timestr}.{codesFileParts[1]}")
    
    if (content_type == 'application/json'):

        with open(codesFile, "w") as outfile:
          json.dump(request.json, outfile, indent = 4)

        codedefs = read_codes()

        return codedefs, 200 
    else:
        return 'Content-Type not supported!', 415