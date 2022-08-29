from marshmallow import Schema, fields

from .answer import AnswerSchema

class QuestionSchema(Schema):
   id = fields.Integer(dump_only=True)
   number = fields.Integer()
   text = fields.String()
   correct_answer = fields.Integer()
   category_id = fields.Integer()
   answers = fields.Nested(AnswerSchema, many=True)


question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)