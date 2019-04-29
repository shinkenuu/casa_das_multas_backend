from flask_restful import fields


state = {
    'id': fields.Integer,
    'name': fields.String,
    'federative_unity': fields.String
}


city = {
    'id': fields.Integer,
    'name': fields.String,
    'cep': fields.String,
    'ibge_code': fields.String,
    'state': fields.Nested(state)
}
