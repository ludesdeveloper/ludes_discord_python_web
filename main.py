from flask import Flask, request, jsonify
from randomize_app import randomize_name

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>Hello, World!</p>"


@app.route("/randomize", methods=['POST'])
def randomize():
    nama = request.json
    data = randomize_name(nama)
    return jsonify(data)


@app.route("/about")
def about():
    return "<p>About!</p>"


if __name__ == "__main__":
    app.run(debug=True)
