from flask import Flask, render_template, send_from_directory, request, jsonify
from database.db import *

app = Flask(__name__)

# Ruta para servir archivos CSS
@app.route('/styles/<path:path>')
def send_css(path):
    return send_from_directory('static/styles', path)

@app.route ("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_func():
    return render_template("register.html")

@app.route("/register_user", methods = ["post"])
def register_render_func():
    data = request.form
    file = request.file
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    photo = file["photo"]
    #add_user(id, name, lastname, birthday)
    upload_file_s3(photo, id)
    print("DATA LLEGANDO ", data)
    return "THE USER WAS ADDED"

@app.route("/consult_page", methods=["GET", "POST"])
def consult_page():
    return render_template("consult.html")

@app.route("/consult_user", methods=["POST"])
def consult_user():
    data = request.get_json()

    id = data.get("id")

    if id is None:
        return "ID no proporcionado", 400

    print("LLEGANDO ID", id)

    result = consult_user_by_id(id)

    if result:
        obj_response = {
            'name' : result[0][1],
            'last_name' : result[0][1]
        }
        print("JSON ES: " + str(result))
        return jsonify(obj_response), 200
    else:
        return "Error al consultar el usuario", 500


if __name__ == "__main__":
    host = "172.31.45.234"
    port = 80
    app.run(host, port)