from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# BASE DE DATOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/oxfactura'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# MODELO DE CLIENTES
class Clients(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        enterprise_id = db.Column(db.String())
        type_document = db.Column(db.String())
        number_doc = db.Column(db.String())
        business_name = db.Column(db.String())
        email = db.Column(db.String())
        phone = db.Column(db.String())
        phone_local = db.Column(db.String())
        country = db.Column(db.String())
        address = db.Column(db.String())
        status = db.Column(db.String())

        def __init__(self,enterprise_id,type_document,number_doc,business_name,email,phone,phone_local,country,address,status):
                self.enterprise_id = enterprise_id
                self.type_document = type_document
                self.number_doc = number_doc
                self.business_name = business_name
                self.email = email
                self.phone = phone
                self.phone_local = phone_local
                self.country = country
                self.address = address
                self.status = status
db.create_all()

# SQUEMA
class ClientSchema(ma.Schema):
        class Meta:
                fields = ('id', 'enterprise_id', 'type_document', 'number_doc', 'business_name', 'email', 'phone', 'phone_local', 'country', 'address', 'departament', 'province', 'district', 'ubigeo', 'status', 'addresses', 'created_at', 'updated_at')

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

# RUTA
appUrl = '/app/v1/clients'

# INDEX
@app.route(appUrl, methods=['GET'])
def all_Clients():
        all_client = Clients.query.all()
        result = clients_schema.dump(all_client)
        return jsonify(result)

# SHOW
@app.route(appUrl+'/<id>', methods=['GET'])
def getClients(id):
        if(request.method == "GET"):
                all_client = Clients.query.get(id)
                result = client_schema.dump(all_client)
                return jsonify(result)

# STORE
@app.route(appUrl, methods=['POST'])
def addClients():
        if(request.method == "POST"):
                data = request.get_json(force=True)
                enterprise_id = data["enterprise_id"]
                type_document = data["type_document"]
                number_doc = data["number_doc"]
                business_name = data["business_name"]
                email = data["email"]
                phone = data["phone"]
                phone_local = data["phone_local"]
                country = data["country"]
                address = data["address"]
                status = data["status"]

                # FORMATEO DE INFORMACION
                business_name = business_name.upper()
                email = email.lower()
                phone_local = phone_local
                country = country.upper()
                address = address.upper()
                # FORMATEO DE INFORMACION

                nuevo_registro=Clients(enterprise_id,type_document,number_doc,business_name,email,phone,phone_local,country,address,status)
                db.session.add(nuevo_registro)
                db.session.commit()
                return client_schema.jsonify(nuevo_registro)

# UPDATE
@app.route(appUrl+'/<id>', methods=['PUT'])
def updateClients(id):
        if(request.method == "PUT"):
                actualizar = Clients.query.get(id)

                data = request.get_json(force=True)
                enterprise_id = data["enterprise_id"]
                type_document = data["type_document"]
                number_doc = data["number_doc"]
                business_name = data["business_name"]
                email = data["email"]
                phone = data["phone"]
                phone_local = data["phone_local"]
                country = data["country"]
                address = data["address"]
                status = data["status"]

                actualizar.enterprise_id = enterprise_id
                actualizar.type_document = type_document
                actualizar.number_doc = number_doc
                actualizar.business_name = business_name.upper()
                actualizar.email = email.lower()
                actualizar.phone = phone
                actualizar.phone_local = phone_local
                actualizar.country = country.upper()
                actualizar.address = address.upper()
                actualizar.status = status

                db.session.commit()
                return client_schema.jsonify(actualizar)

# DELETE
@app.route(appUrl+'/<id>', methods=['DELETE'])
def destroyClients(id):
        if(request.method == "DELETE"):
                eliminar = Clients.query.get(id)
                db.session.delete(eliminar)
                db.session.commit()
                return client_schema.jsonify(eliminar)

app.run(debug=True)