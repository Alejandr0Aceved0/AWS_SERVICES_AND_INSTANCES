import pymysql

db_host = "instancia-bd-prueba-290.chsew4ku8tz8.us-east-1.rds.amazonaws.com"
db_user = "alejandro"
db_pass = "ROCKO2024*"

try:

        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password= db_pass
        )
        print("CONEXION A BD EXITOSA")

except Exception as e:

        connection = None
        print("ERROR EN CONECTAR A LA BD, ERROR ES: ", e)


def add_user(id, name, lastname, birthday):
    
    use_database = "USE db_users;"

    try:
        cursor = connection.cursor()
        cursor.execute(use_database)
        connection.commit()
        print("BD USADA")

    except Exception as e:
        print("ERROR EN AL USAR BD, ERROR ES: ", e)


    instruction_sql = "INSERT INTO users(id, name, last_name, birthday) VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"',);"
    
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("USUARIO AGREGADO")

    except Exception as e:
        print("ERROR EN AL INSERTAR EL REGISTRO, ERROR ES: ", e)


def consult_user_by_id(id):
    use_database = "USE db_users;"

    try:
        cursor = connection.cursor()
        cursor.execute(use_database)
        connection.commit()
        print("BD USADA")

    except Exception as e:
        print("ERROR EN AL USAR BD, ERROR ES: ", e)
              
    instruction_sql = "SELECT * FROM users WHERE id = %s;"
    
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql, (id,))  # Usa una tupla para pasar el parámetro
        result = cursor.fetchall()
        print("HACIENDO CONSULTA POR ID:", id)
        print("RESULTADO ES: ", result)
        return result

    except Exception as e:
        print("ERROR EN LA CONSULTA, ERROR ES:", e)
        return None  # Retorna None o maneja el error de otra manera
    finally:
        cursor.close()  # Asegúrate de cerrar el cursor si ya no lo necesitas

