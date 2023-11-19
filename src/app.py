#!/usr/bin/env python3
from sys import argv
from flask import Flask, render_template, redirect
from dataclasses import dataclass
import werkzeug
from waitress import serve


app = Flask(__name__)
app.secret_key = argv[1].encode()
DEBUG = True

@dataclass
class ErrorData:
    code: int
    message: str


@app.route("/index")
@app.route("/index.html")
@app.route("/index.htm")
@app.route("/main")
def redirect_to_root():
    return redirect("/", code=302)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return "nothing here yet!"


@app.route("/signin")
def signin():
    return "nothing here yet!"

def handle_bad_request(e):
    data = ErrorData(400, "bad request")
    return render_template("error.html", context=data), 400

app.register_error_handler(400, handle_bad_request)

def handle_missing_page(e):
    data = ErrorData(404, "page not found")
    return render_template("error.html", context=data), 404

app.register_error_handler(404, handle_missing_page)

if DEBUG:
    app.run(debug=True)
else:
    serve(app, host="127.0.0.1", port=5000)
