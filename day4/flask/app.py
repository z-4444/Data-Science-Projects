from flask import Flask
# import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Muhammad Zahid"

app.run(host = '0.0.0.0')