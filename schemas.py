from flask_restful import fields

STATE_SCHEMA = {
    'id': fields.Integer,
    'name': fields.String,
    'federative_unity': fields.String,
    'ibge_code': fields.String,
}

CITY_SCHEMA = {
    'id': fields.Integer,
    'name': fields.String,
    'ibge_code': fields.String,
    'state_id': fields.Integer,
}

LOCATION_SCHEMA = {
    'public_name': fields.String,
    'number': fields.String,
    'neighborhood': fields.String,
    'reference': fields.String,
    'zip_code': fields.String,
    'city': fields.Nested(CITY_SCHEMA),
    'state': fields.Nested(STATE_SCHEMA)
}

PERSON_SCHEMA = {
    'id': fields.Integer,
    'uid': fields.String,
    'updated_at': fields.DateTime(dt_format='iso8601'),

    'legal_type': fields.String,
    'name': fields.String,
    'nickname': fields.String,
    'rg_ie': fields.String,
    'cpf_cnpj': fields.String,

    'partner_types': fields.List(fields.String),

    'contact': {
        'name_1': fields.String(attribute='contact_1'),
        'name_2': fields.String(attribute='contact_2'),
        'phone_1': fields.String(),
        'phone_2': fields.String(),
        'fax': fields.String(),
        'cellphone': fields.String(),
        'email': fields.String,
        'email_nfe': fields.String,
    },

    'location': {
        'public_name': fields.String,
        'number': fields.String(attribute='address_number'),
        'neighborhood': fields.String,
        'reference': fields.String(attribute='address_reference'),
        'zip_code': fields.String,
        'city': {
            'id': fields.String(attribute='city.id'),
            'name': fields.String(attribute='city.name'),
            'ibge_code': fields.String(attribute='city.ibge_code'),
        },
        'state': {
            'id': fields.String(attribute='city.state.id'),
            'name': fields.String(attribute='city.state.name'),
            'federative_unity': fields.String(attribute='city.state.federative_unity'),
            'ibge_code': fields.String(attribute='city.state.ibge_code'),
        }
    },

    'observation': fields.String,
    'is_incomplete_data': fields.Boolean,
}
