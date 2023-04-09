from marshmallow import Schema, fields


class PredictSchema(Schema):
    age = fields.Integer(required=True)
    salary = fields.Integer(required=True)
