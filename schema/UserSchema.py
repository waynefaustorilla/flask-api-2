from marshmallow import Schema
from marshmallow import fields

class UserSchema(Schema):
  firstname = fields.Str(required=True)
  middlename = fields.Str(required=True)
  lastname = fields.Str(required=True)
  username = fields.Str(required=True)
  email = fields.Str(required=True)
  password = fields.Str(required=True, load_only=True)
  repeat_password = fields.Str(required=True, load_only=True)
  date_created = fields.Str(dump_only=True)

class UserUpdateSchema(Schema):
  firstname = fields.Str(required=False)
  middlename = fields.Str(required=False)
  lastname = fields.Str(required=False)
  username = fields.Str(required=False)
  email = fields.Str(required=False)
  password = fields.Str(required=False)