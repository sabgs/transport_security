from ..core.ext import db

class Category(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   number = db.Column(db.Integer, nullable=False)
   questions = db.relationship('Question', lazy=False)

   def __init__(self, number: int):
      self.number = number

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