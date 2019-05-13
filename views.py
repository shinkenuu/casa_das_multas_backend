from flask import request
from flask_restful import abort, marshal_with, Resource

from models.people import Person
from models.locations import City, State
from schemas import CITY_SCHEMA, STATE_SCHEMA, PERSON_SCHEMA


class PeopleListResource(Resource):
    def post(self):
        return None, 204


class PeopleResource(Resource):
    @marshal_with(PERSON_SCHEMA)
    def get(self, people_id: int):
        person = Person.query.get(people_id)

        if not person:
            abort(404, message='person not found')

        return person

    def put(self, people_id: int):
        return None, 204

    def delete(self, people_id: int):
        return None, 204


class CityResource(Resource):
    @marshal_with(CITY_SCHEMA)
    def get(self):
        ibge_code = request.args.get('ibge_code')

        if not ibge_code or not ibge_code.isdigit():
            abort(400, message='invalid parameter "ibge_code"')

        city = City.query.filter_by(ibge_code=int(ibge_code)).first()
        
        if not city:
            abort(404, message='city not found')
        
        return city


class StateResource(Resource):
    @marshal_with(STATE_SCHEMA)
    def get(self):
        ibge_code = request.args.get('ibge_code')

        if not ibge_code or not ibge_code.isdigit():
            abort(400, message='invalid parameter "ibge_code"')

        state = State.query.filter_by(ibge_code=int(ibge_code)).first()
        
        if not state:
            abort(404, message='state not found')
        
        return state
