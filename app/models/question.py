from ..core.ext import db

correct_answers = db.Table('correct_answers',
   db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
   db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'), primary_key=True)
)
class Question(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   number = db.Column(db.Integer, nullable=False)
   text = db.Column(db.Text, nullable=False)
   correct_answer = db.relationship('Answer', secondary=correct_answers, lazy=False, backref=db.backref('questions', lazy=True))
   category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
   answers = db.relationship('Answer', lazy=False)


   @classmethod
   def get_all(cls):
      return cls.query.all()

   @classmethod
   def get_by_id(cls, id):
      return cls.query.get_or_404(id)

   @classmethod
   def get_by_number(cls, number):
      return cls.query.filter_by(number=number).first()

   def save(self):
      db.session.add(self)
      db.session.commit()

   def flush(self):
      db.session.add(self)
      db.session.flush()

   def delete(self):
      db.session.delete(self)
      db.session.commit()