from flask import Flask, request, redirect, render_template
from cs50 import SQL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/start")
def start():
    return render_template("pocetna.html")