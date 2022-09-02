from marshmallow import ValidationError

from ...models.question import Question
from ...models.answer import Answer
from ...schemas.question import question_schema, questions_schema
from ...schemas.answer import answer_schema, answers_schema
from ...schemas.request_data import request_schema, requests_schema

def get_all():
   all_questions = Question.get_all()

   return questions_schema.dump(all_questions)

def get_normolize_data(data):
   normalize_data = request_schema.dump(request_schema.load(data))
   return normalize_data


def create_answer(data):
   try:
      valid_data = answer_schema.load(data)
   except ValidationError as err:
      return err.messages

   answer = Answer(text = valid_data['text'])

   return answer

def create_question(data: dict):
   try:
      normolize_data = get_normolize_data(data)
      valid_data = question_schema.load(normolize_data)
   except ValidationError as err:
      return err.messages
   category = Question(number=valid_data['number'],
                       text=valid_data['text'],
                       correct_answer=valid_data['correct_answer'],
                       category_id=valid_data['category_id']
                  )
   if valid_data['answers']:
      for answer in valid_data['answers']:
         answer = create_answer(answer)
         category.answers.append(answer)

   category.save()

   return category

def create(data: dict | list):
   # print(requests_schema.load(data))
   if type(data) == list:
      questions_list = []
      for question in data:
         questions_list.append(create_question(question))
      return questions_schema.dump(questions_list)

   question = create_question(data)

   return question_schema.dump(question)