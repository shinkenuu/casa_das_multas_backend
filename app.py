from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask('casa_das_multas')
app.config.from_object('config')
CORS(app)

api = Api(app)

db = SQLAlchemy(app)


from views import CityResource, StateResource, PeopleResource, PeopleListResource

api.add_resource(PeopleListResource, '/people/')
api.add_resource(PeopleResource, '/people/<int:people_id>')
api.add_resource(CityResource, '/cities')
api.add_resource(StateResource, '/states')
