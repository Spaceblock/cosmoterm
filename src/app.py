#!/usr/bin/env python3
from sys import argv
from flask import Flask, render_template
from waitress import serve


app = Flask(__name__)
app.secret_key = argv[1].encode()
DEBUG = True


@app.route("/")
def home():
    return render_template("home.html")


if DEBUG:
    app.run(debug=True)
else:
    serve(app, host="127.0.0.1", port=5000)