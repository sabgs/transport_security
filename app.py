from datetime import datetime
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


cors = CORS(app, resources={r"/*": {"origins": "*"}})


class TimestampMixin(object):
    created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)


class Category(TimestampMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(30), nullable=False)
   questions = db.relationship('Question', lazy=False)

   def serialize(self):
      return {
         'name': f'{self.name} категория',
         'questions': [question.serialize() for question in self.questions]
      }


class Question(TimestampMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   number = db.Column(db.String(5), nullable=False)
   text = db.Column(db.String(255), nullable=False)
   category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
   correct_answer = db.Column(db.String(5))
   answers = db.relationship('Answer', lazy=False)


   def serialize(self):
      return {
         'id': self.id,
         'number': self.number,
         'text': self.text,
         'answers': [answer.serialize() for answer in self.answers],
         'correct_answer': {
            'answer': self.answers[int(self.correct_answer)].serialize(),
            'value': int(self.correct_answer) + 1
            }
      }


class Answer(TimestampMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   text = db.Column(db.String(255), nullable=False)
   question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

   def serialize(self):
      return {
         'id': self.id,
         'text': self.text
      }


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/categories', methods=['GET', 'POST'])
def categories():
   if request.method == 'POST':
      data = request.get_json()
      cat = Category(name=data['category'])
      db.session.add(cat)
      db.session.commit()
      return 'category add'
   return '1'


@app.route('/categories/<number>', methods=['GET'])
def category(number):
   category = Category.query.filter_by(name=number).first()
   return jsonify(data=[question.serialize() for question in category.questions])


@app.route('/questions', methods=['GET', 'POST'])
def questions():
   if request.method == 'POST':
      data = request.get_json()
      for q in data:
         try:
            quest_text = re.findall(r"^(\d+)\.*\s*([\w\s\.()№\-\–\—«»,/]*)", q['quest_text'])[0]

            q_number = quest_text[0]
            q_text = quest_text[1]

            qu = Question.query.filter_by(text=q_text).first()

            if qu:
               raise ValueError('Quest is exists!')

            new_quest = Question(number=q_number, text=q_text, category_id=1)

            # !Возможны ли повторы вопросов?
            # try:
            #    if not q['correct_answer'] is None:
            #       new_quest.correct_answer = q['correct_answer']
            # except:
            #    print('not corr answ')

            db.session.add(new_quest)
            db.session.flush()
            for a in q['answers']:
               answer_text = re.findall(r"^\s+\d+.|.\s+([\w\s,./«»()\-\–\—]+)", a)[1].strip()
               new_answer = Answer(text=answer_text, question_id=new_quest.id)
               db.session.add(new_answer)
            db.session.commit()
            print(f'Вопрос №{q_number} добавлен!')
         except Exception as ex:
            print(str(ex))
      return '2'
   return '1'

@app.route('/questions/<number>', methods=['GET', 'POST'])
def question(number):
   quest = Question.query.filter_by(number=number).first()

   if quest is None:
      return 'quest is not exists!'

   return jsonify(data=quest.serialize())

if __name__ == '__main__':
   db.create_all()