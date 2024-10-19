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


def add_user():
    
    use_database = "USE db_users;"

    try:
        cursor = connection.cursor()
        cursor.execute(use_database)
        connection.commit()
        print("BD USADA")

    except Exception as e:
        print("ERROR EN AL USAR BD, ERROR ES: ", e)


    instruction_sql = "INSERT INTO user(id, name, last_name, birthday) VALUES (456, 'CARLOS', 'ACEVEDO', '1998-29-08');"
    
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("USUARIO AGREGADO")

    except Exception as e:
        print("ERROR EN AL INSERTAR EL REGISTRO, ERROR ES: ", e)


add_user()