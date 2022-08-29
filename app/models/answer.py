from ..core.ext import db

class Answer(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   text = db.Column(db.String(255), nullable=False)
   question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)

   # def __init__(self, text: str):
   #    self.text = text

   @classmethod
   def get_all(cls):
      return cls.query.all()

   @classmethod
   def get_by_id(cls, id):
      return cls.query.get_or_404(id)

   def save(self):
      db.session.add(self)
      db.session.commit()

   def flush(self):
      db.session.add(self)
      db.session.flush()

   def delete(self):
      db.session.delete(self)
      db.session.commit()