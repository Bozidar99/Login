from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/singup")
def index():
    return render_template("singup.html")