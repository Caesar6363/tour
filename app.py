from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!11"


@app.route("/user", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request)
        return "POST"
    else:
        return "GET"
