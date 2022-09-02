from marshmallow import ValidationError

from ...models.category import Category
from ...schemas.category import category_schema, categories_schema
from ...schemas.question import questions_schema_db

def get_all():
   app_categories = Category.get_all()

   return categories_schema.dump(app_categories)


def create(data: dict):
   try:
      valid_data = category_schema.load(data)
   except ValidationError as err:
      return err.messages

   category = Category.get_by_number(valid_data['number'])
   if category:
      return 'Category is exists!'

   category = Category(valid_data['number'])
   category.save()

   return category_schema.dump(category)

def get_one_by_number(number):
   category = Category.get_by_number(number)

   return category_schema.dump(category)

def get_all_questions_for_category(number):
   category = Category.get_by_number(number)
   return questions_schema_db.dump(category.questions)