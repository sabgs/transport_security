from marshmallow import ValidationError

from ...models.question import Question
from ...models.answer import Answer
from ...schemas.question import question_schema, questions_schema
from ...schemas.answer import answer_schema, answers_schema

def get_all():
   all_questions = Question.get_all()

   return questions_schema.dump(all_questions)

# def normolize_data(data):


def create_answer(data):
   try:
      valid_data = answer_schema.load(data)
   except ValidationError as err:
      return err.messages

   answer = Answer(text = valid_data['text'])

   return answer

def create_question(data: dict):
   try:
      valid_data = question_schema.load(data)
   except ValidationError as err:
      return err.messages

   category = Question(number=valid_data['number'],
                       text=valid_data['text'],
                       correct_answer=valid_data['correct_answer'],
                       category_id=valid_data['category_id']
                  )
   if data['answers']:
      for answer in data['answers']:
         answer = create_answer(answer)
         category.answers.append(answer)

   category.save()

   return category

def create(data: dict | list):
   print(type(data) == list)
   if type(data) == list:
      questions_list = []
      for question in data:
         questions_list.append(create_question(question))
      return questions_schema.dump(questions_list)

   question = create_question(data)

   return question_schema.dump(question)