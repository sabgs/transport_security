import re
from marshmallow import Schema, fields

# TODO Доделать!
class RequestSchema(Schema):
   question_text = fields.String(load_only=True)
   answers_list = fields.List(fields.String(), load_only=True)
   correct_answer = fields.Integer()

   number = fields.Method('normolize_question_number', dump_only=True)
   text = fields.Method('normolize_question_text', dump_only=True)
   answers = fields.Method('normolize_answers_text', dump_only=True)


   def normolize_question_number(self, obj):
      quest_text = re.findall(r"^(\d+)\.*\s*([\w\s\.()№\-\–\—«»,/]*)", obj['question_text'])[0]
      return int(quest_text[0])

   def normolize_question_text(self, obj):
      quest_text = re.findall(r"^(\d+)\.*\s*([\w\s\.()№\-\–\—«»,/]*)", obj['question_text'])[0]
      return quest_text[1]

   def normolize_answers_text(self, obj):
      answers_list = []
      for answer in obj['answers_list']:
         answer_text = re.findall(r"^\s+\d+.|.\s+([\w\s,./«»()\-\–\—]+)", answer)[1].strip()
         answers_list.append(answer_text)
      return answers_list


