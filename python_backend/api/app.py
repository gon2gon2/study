from flask import Flask

app = Flask('__name__')

@app.route("/ping", methods=['GET'])   # route decorator, GET method
def ping():
    return "pong"
