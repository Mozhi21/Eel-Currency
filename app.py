from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")


@app.route("/")
def home():
    return "Home Page Route test github"


@app.route("/about")
def about():
    return "About Page Route"


@app.route("/portfolio")
def portfolio():
    return "Portfolio Page Route"


@app.route("/contact")
def contact():
    return "Contact Page Route"


@app.route("/api")
def api():
    from data import sample

    return sample
