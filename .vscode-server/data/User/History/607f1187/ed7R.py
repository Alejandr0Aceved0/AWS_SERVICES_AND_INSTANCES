from flask import Flask, render_template
from database import *

app = Flask(__name__)

@app.route ("/")

def home_func():
    return render_template("home.html")

@app.route("/register_page")

def register_page_func():
    return render_template("register.html")

@app.route("/register_user")
def register_user_func():
    return "THE USER WAS ADDED"


@app.route("/consult_page")

def consult_page_func():
    return "vista de consulta"

if __name__ == "__main__":
    host = "172.31.45.234"
    port = "80"
    app.run(host, port)