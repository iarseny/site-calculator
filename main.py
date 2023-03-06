
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

number1 = None
number2 = None
number3 = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/count", methods=["POST"])
def count():
    print(request.form)
    return jsonify({1: 123})

if __name__ == "__main__":
    app.run()
