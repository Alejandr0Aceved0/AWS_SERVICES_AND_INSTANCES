from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route ("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_func():
    return render_template("register.html")

@app.route("/register_user", methods = ["post"])
def register_render_func():
    data = request.form
    print("DATA LLEGANDO ", data)
    return "THE USER WAS ADDED"

if __name__ == "__main__":
    host = "172.31.45.234"
    port = 80
    app.run(host, port)