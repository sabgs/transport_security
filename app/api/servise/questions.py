from marshmallow import ValidationError

from ...models.question import Question
from ...models.answer import Answer
from ...schemas.question import question_schema, question_schema_db, questions_schema_db
from ...schemas.answer import answer_schema

def get_all():
   all_questions = Question.get_all()

   return questions_schema_db.dump(all_questions)

def get_single_question(id):
   question = Question.get_by_id(id)

   return question_schema_db.dump(question)


def create_answer(data):
   try:
      valid_data = answer_schema.load(data)
   except ValidationError as err:
      return err.messages

   answer = Answer(text = valid_data['text'])

   return answer

def create_question(data: dict):
   try:
      valid_data = question_schema.dump(question_schema.load(data))
   except ValidationError as err:
      return err.messages
   question = Question(number=valid_data['number'],
                       text=valid_data['text'],
                       category_id=valid_data['category_id']
                  )
   if valid_data['answers']:
      for i, answer in enumerate(valid_data['answers']):
         answer = create_answer(answer)
         if i == valid_data['correct_answer']:
            question.correct_answer.append(answer)
         question.answers.append(answer)

   question.save()

   return question

def create(data: dict | list):
   if type(data) == list:
      questions_list = []
      for question in data:
         questions_list.append(create_question(question))
      return questions_schema_db.dump(questions_list)

   question = create_question(data)

   return question_schema_db.dump(question)