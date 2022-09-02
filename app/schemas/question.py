import re

from marshmallow import Schema, fields

from .answer import answers_schema


class QuestionSchemaDB(Schema):
   id = fields.Integer()
   number = fields.Integer()
   text = fields.String()
   correct_answer = fields.Method('get_correct_answer')

   def get_correct_answer(self, obj):
      answer = answers_schema.dump(obj.correct_answer)
      return answer

class QuestionSchema(Schema):
   question_text = fields.String()
   correct_answer = fields.Integer()
   category_id = fields.Integer()
   answers_list = fields.List(fields.String())

   number = fields.Method('normolize_question_number', dump_only=True)
   text = fields.Method('normolize_question_text', dump_only=True)
   answers = fields.Method('normolize_answers_text', dump_only=True)


   def normolize_question_number(self, obj):
      print(obj)
      quest_text = re.findall(r"^\s*\D*(\d+)*\.*\:*\s*([\w\s\.()№\-\–\—«»,\/]*)", obj['question_text'])[0]
      return int(quest_text[0])

   def normolize_question_text(self, obj):
      quest_text = re.findall(r"^\s*\D*(\d+)*\.*\:*\s*([\w\s\.()№\-\–\—«»,\/]*)", obj['question_text'])[0]
      return quest_text[1]

   def normolize_answers_text(self, obj):
      answers_list = []
      for answer in obj['answers_list']:
         answer_text = re.findall(r"^\s+\d+.|.\s+([\w\s\d,./«»()\-\–\—]+)", answer)[1].strip()
         answers_list.append({'text': answer_text})
      return answers_list



question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)

question_schema_db = QuestionSchemaDB()
questions_schema_db = QuestionSchemaDB(many=True)