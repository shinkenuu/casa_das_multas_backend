from marshmallow import INCLUDE, fields, post_load, pre_dump, Schema

from models.locations import City
from models.people import Person
from schemas.locations import LocationSchema


class ContactSchema(Schema):
    name_1 = fields.Str(allow_none=True)
    name_2 = fields.Str(allow_none=True)
    phone_1 = fields.Str(allow_none=True)
    phone_2 = fields.Str(allow_none=True)
    fax = fields.Str(allow_none=True)
    cellphone = fields.Str(allow_none=True)
    email = fields.Str(allow_none=True)
    email_nfe = fields.Str(allow_none=True)


class PersonSchema(Schema):
    class Meta:
        unknown = INCLUDE

    id = fields.Int(dump_only=True, required=True)
    uid = fields.Str(allow_none=True)
    updated_at = fields.DateTime(dump_only=True, allow_none=True)

    legal_type = fields.Str(allow_none=True)
    name = fields.Str(allow_none=True)
    nickname = fields.Str(allow_none=True)
    rg_ie = fields.Str(allow_none=True)
    cpf_cnpj = fields.Str(allow_none=True)

    partner_types = fields.List(fields.Str(), required=True)

    contact = fields.Nested(ContactSchema, required=True)

    location = fields.Nested(LocationSchema, required=True)

    observation = fields.Str(allow_none=True)
    is_incomplete_data = fields.Bool(allow_none=True)

    @pre_dump
    def _pre_dump(self, person: Person):
        person.contact = {
            'name_1': person.contact_1,
            'name_2': person.contact_2,
            'phone_1': person.phone_1,
            'phone_2': person.phone_2,
            'fax': person.fax,
            'cellphone': person.cellphone,
            'email': person.email,
            'email_nfe': person.email_nfe,
        }

        person_city = person.city

        city = {
            'id': person_city.id,
            'name': person_city.name,
            'ibge_code': person_city.ibge_code,
            'state_id': person_city.state_id,
        }

        person_state = person.city.state

        state = {
            'id': person_state.id,
            'name': person_state.name,
            'federative_unity': person_state.federative_unity,
            'ibge_code': person_state.ibge_code,
        }

        person.location = {
            'public_name': person.public_name,
            'number': person.address_number,
            'neighborhood': person.neighborhood,
            'reference': person.address_reference,
            'zip_code': person.zip_code,
            'city': city,
            'state': state,
        }

        return person

    @post_load
    def _post_load(self, item):
        city_id = item['location']['city']['id']
        city = City.query.get(city_id)

        contact = item['contact']
        location = item['location']

        person_kwargs = {
            'legal_type': item.get('legal_type'),
            'name': item.get('name'),
            'nickname': item.get('nickname'),
            'rg_ie': item.get('rg_ie'),
            'cpf_cnpj': item.get('cpf_cnpj'),

            'partner_types': item.get('partner_types'),

            'public_name': location.get('public_name'),
            'address_number': location.get('number'),
            'neighborhood': location.get('neighborhood'),
            'address_reference': location.get('reference'),
            'zip_code': location.get('zip_code'),

            'city': city,

            'phone_1': contact.get('phone_1'),
            'contact_1': contact.get('name_1'),
            'phone_2': contact.get('phone_2'),
            'contact_2': contact.get('name_2'),
            'email': contact.get('email'),
            'email_nfe': contact.get('email_nfe'),

            'is_incomplete_data': item.get('is_incomplete_data'),
        }

        id = item.get('id')

        person = Person.query.get(id) if id else Person()
        person.update(person_kwargs)

        return person
