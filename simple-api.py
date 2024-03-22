from flask import Flask
import json

app = Flask(__name__)

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

@app.route("/hello/<username>")
def hello_world(username):
    return f"<p>Hello, {username}!</p>"


@app.route('/hello-json')
def send_json():
    data = {
        "name": "Raghav",
        "age": 30,
        "city": "Berkeley"
    }
    return json.dumps(data)

