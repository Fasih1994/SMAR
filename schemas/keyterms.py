from marshmallow import Schema, fields


class KeytermGenSchema(Schema):
    id = fields.Int()
    text = fields.Str(required=True)
    terms = fields.List(cls_or_instance=fields.Str(), dump_only=True,)