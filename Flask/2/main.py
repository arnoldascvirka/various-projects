from urllib import request
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return render_template("index.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
