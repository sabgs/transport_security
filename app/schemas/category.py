from marshmallow import Schema, fields

from .question import QuestionSchema

class CategorySchema(Schema):
   id = fields.Integer(dump_only=True)
   number = fields.Integer()
   questions = fields.Nested(QuestionSchema, many=True)


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)