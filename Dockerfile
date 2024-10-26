#sudo yum install docker

FROM python:latest

WORKDIR /project

COPY . /project

#INSTALACION DE DEPENDENCIAS CUANDO ES UN PROYECTO PEQUEÑO
# COLOCAMOS INSTALACION MANUAL UNA A UNA

# RUN pip install pymysql
# RUN pip install boto3

# Podemos usar el siguiente comando
# pip freeze> requeriments.txt
# nos genera un archivmos llamado requeriments.txt, donde nos trae todas las dependencias que tiene nuestro proyecto

# Para instalar casi de forma automatica hacemos lo siguiente, (teniendo el archivo requerminets.txt previamente)
# RUN pip install -r requeriments.txt

RUN pip install -r requeriments.txt

#instruccion por consola
CMD ["python", "server.py"]