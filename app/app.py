from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World! How are you doing? Doing fine!!! TEST TEST2"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
