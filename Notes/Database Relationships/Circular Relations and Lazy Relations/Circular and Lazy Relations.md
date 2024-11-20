# Circular Relations & Lazy Relations

Sometimes, you might have two models that depend on each other - i.e. you end up with a circular relationship.

Or you have a model that has a relation with itself.

Or you have a model that should have a relation with some built-in model (i.e. built into Django) or a model defined in another application.

Below, you find examples for all three cases that include Django's solution for these kinds of "problems": Lazy relationships. You can also check out the official docs in addition.

1) Two models that have a circular relationship

class Product(models.Model):
  # ... other fields ...
  last_buyer = models.ForeignKey('User')
  
class User(models.Model):
  # ... other fields ...
  created_products = models.ManyToManyField('Product')
In this example, we have multiple relationships between the same two models. Hence we might need to define them in both models. By using the model name as a string instead of a direct reference, Django is able to resolve such dependencies.

2) Relation with the same model

class User(models.Model):
  # ... other fields ...
  friends = models.ManyToManyField('self') 
The special self keyword (used as a string value) tells Django that it should form a relationship with (other) instances of the same model.

3) Relationships with other apps and their models (built-in or custom apps)

class Review(models.Model):
  # ... other fields ...
  product = models.ForeignKey('store.Product') # '<appname>.<modelname>'
You can reference models defined in other Django apps (no matter if created by you, via python manage.py startapp <appname> or if it's a built-in or third-party app) by using the app name and then the name of the model inside the app.