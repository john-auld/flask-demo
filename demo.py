'''
Simple flask demo app to show how to run
gunicorn within a virtualenv using a systemd unit file 

Tested on CentOS 7
'''
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return 'OK', 200


### Start up settings
if __name__ == "__main__":
    app.run()