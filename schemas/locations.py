from marshmallow import fields, Schema


class StateSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    federative_unity = fields.Str()
    ibge_code = fields.Str(required=True)


class CitySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str()
    ibge_code = fields.Str(required=True)
    state_id = fields.Int()


class LocationSchema(Schema):
    public_name = fields.Str(allow_none=True)
    number = fields.Str(allow_none=True)
    neighborhood = fields.Str(allow_none=True)
    reference = fields.Str(allow_none=True)
    zip_code = fields.Str(allow_none=True)
    city = fields.Nested(CitySchema)
    state = fields.Nested(StateSchema)
