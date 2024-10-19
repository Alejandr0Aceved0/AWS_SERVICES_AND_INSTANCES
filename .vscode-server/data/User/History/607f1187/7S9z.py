from flask import Flask, render_template, request
from database import *

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


@app.route("/consult_page")

def consult_page_func():
    return "vista de consulta"

if __name__ == "__main__":
    host = "172.31.45.234"  # Puedes cambiar esto a '0.0.0.0' para permitir el acceso externo
    port = 5000  # Cambiado de 80 a 5000
    app.run(host, port)