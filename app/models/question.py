from ..core.ext import db

class Question(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   number = db.Column(db.Integer, nullable=False)
   text = db.Column(db.Text, nullable=False)
   correct_answer = db.Column(db.Integer)
   category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
   answers = db.relationship('Answer', lazy=False)

   def __init__(self, number: int, text: str, correct_answer: int, category_id: int):
      self.number = number
      self.text = text
      self.correct_answer = correct_answer
      self.category_id = category_id

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