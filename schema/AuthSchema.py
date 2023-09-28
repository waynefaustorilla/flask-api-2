from marshmallow import Schema
from marshmallow import fields

class AuthSchema(Schema):
  username = fields.Str(required=True)
  password = fields.Str(required=True)