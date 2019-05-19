from datetime import datetime

from flask import request
from flask_restful import abort, Resource

from app import db
from models.people import Person
from models.locations import City
from schemas.locations import CitySchema
from schemas.people import PersonSchema


class PeopleListResource(Resource):
    schema = PersonSchema()

    def post(self):
        schema_errors = self.schema.validate(request.json)

        if schema_errors:
            return schema_errors, 400

        person = self.schema.load(request.json)

        db.session.add(person)
        db.session.commit()

        serialized_person = self.schema.dump(person)
        return serialized_person, 201


class PeopleResource(Resource):
    schema = PersonSchema()

    def get(self, people_id: int):
        person = Person.query.get(people_id)

        if not person:
            abort(404, message='person not found')

        serialized_person = self.schema.dump(person)
        return serialized_person, 200

    def put(self, people_id: int):
        schema_errors = self.schema.validate(request.json)

        if schema_errors:
            return schema_errors, 400

        payload = {
            **request.json,
            'id': people_id,
        }

        person = self.schema.load(payload)

        if not person.id:
            abort(404, message='person not found')

        person.updated_at = datetime.now()

        db.session.add(person)
        db.session.commit()

        serialized_person = self.schema.dump(person)
        return serialized_person, 200

    def delete(self, people_id: int):
        person = Person.query.get(people_id)

        if not person:
            abort(404, message='person not found')

        db.session.delete(person)
        db.session.commit()

        return None, 204


class CityResource(Resource):
    schema = CitySchema()

    def get(self):
        city_name = request.args.get('name')

        if not city_name:
            abort(400, message='invalid parameter "name"')
            return

        city = City.query.filter_by(name=city_name).first()

        if not city:
            abort(404, message='city not found')
            return

        serialized_city = self.schema.dump(city)
        return serialized_city
