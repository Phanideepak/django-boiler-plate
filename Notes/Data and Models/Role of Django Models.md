# Role of Django Models

- Models in Django are Python classes that are used to define the structure of database tables.
- Django Models translates Python query logic into SQL Queries.
- Meta data can be added by using inner Meta class

Eg: 

from django.db import models

class Student(models.Model):
    id = models.IntegerField()
    firstname = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'Student Entries'
