from flask_restful import marshal_with, Resource

from models.locations import City
from schemas import city as city_schema


class PeopleListResource(Resource):
    def post(self):
        return None, 204


class PeopleResource(Resource):
    def get(self, people_id: int):
        return None, 204

    def put(self, people_id: int):
        return None, 204

    def delete(self, people_id: int):
        return None, 204


class LocationListResource(Resource):
    @marshal_with(city_schema)
    def get(self):
        cities = City.query.all()
        return cities
