from traceback import print_tb
from typing import List
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

# Mensaje de Bienvenida
@app.route('/welcome',methods=['GET'])
def welcome():
        return jsonify({'Mensaje':'Backend APIRest Python'})

appUrl = '/app/v1/users'
ListUser = [
                {"id": "0", "nombre": "NOMBRE1", "apellido": "APELLIDO1"},
                {"id": "1", "nombre": "NOMBRE2", "apellido": "APELLIDO2"},
                {"id": "2", "nombre": "NOMBRE3", "apellido": "APELLIDO3"}
           ]

# INDEX
@app.route(appUrl, methods=['GET'])
def index_User():
        if(request.method == "GET"):
                return jsonify(ListUser)

# SHOW
@app.route(appUrl+'/<id>', methods=['GET'])
def getUser(id):
        if(request.method == "GET"):
                return jsonify(ListUser[int(id)])

# STORE
@app.route(appUrl, methods=['POST'])
def addUser():
        if(request.method == "POST"):
                user = {"id": request.json["id"], "nombre": request.json["nombre"], "apellido": request.json["apellido"]}
                ListUser.append(user)
                return jsonify(user["nombre"])

# UPDATE
@app.route(appUrl+'/<id>', methods=['PUT'])
def updateUser(id):
        if(request.method == "PUT"):
                user = {"nombre": request.json["nombre"], "apellido": request.json["apellido"]}
                ListUser.append(user)
                return jsonify(user["nombre"])

# DELETE
@app.route(appUrl+'/<id>', methods=['DELETE'])
def destroyUser(id):
        if(request.method == "DELETE"):
                return 'Eliminado Correctamente el id:' + id

app.run(debug=True)