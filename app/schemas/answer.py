from marshmallow import Schema, fields

class AnswerSchema(Schema):
   id = fields.Integer(dump_only=True)
   text = fields.String()
   # question_id = fields.Integer(load_only=True)


answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)