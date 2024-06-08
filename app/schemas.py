from marshmallow import Schema, fields


class NodeInputSchema(Schema):
    parent_id = fields.Integer(required=True)
    name = fields.String(required=True)


node_input_schema = NodeInputSchema()