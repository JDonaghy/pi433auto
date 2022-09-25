# Import the flask library
from flask import Flask, request, Response, send_file
from flask_cors import CORS
import json
import shutil
import time
import subprocess

from shelljob import proc


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


@app.route('/stream2')
def execute():
    exec_path = "transceiver/receive.py"
    cmd = [ "bash", "-c", f"python {exec_path}" ]  # -u: don't buffer output

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
    )
    def read_process():
      for line in proc.stdout:
          yield line

    return Response( read_process(), mimetype= 'text/event-stream' )



@app.route( '/stream' )
def stream():
    exec_path = "transceiver/receive.py"
    g = proc.Group()
    p = g.run( [ "bash", "-c", f"python {exec_path}" ] )

    def read_process():
        while g.is_pending():   
            lines = g.readlines()
            print (f"lines {str(lines)}")
            for proc, line in lines:
                yield line

    return Response( read_process(), mimetype= 'text/event-stream' )

@app.route('/streampage')
def get_page():
    return send_file('streampage.html')

if __name__ == "__main__":
    app.run(debug=True)