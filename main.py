from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return "<p>About!</p>"


if __name__ == "__main__":
    app.run(debug=True)
