# Read Models

- SELECT * FROM books ----> Book.objects.all()

- Filtering By Column nane ---> Book.objects.get(column_name = given_name)

- Filtering By multiple columns (AND) ---> Book.objects.get(col1 = val1, col2 = val2)

- Filtering by column less than val ---> Book.objects.get(col1__lt = val)

- Filtering by column less than or equal to val ---> Book.objects.get(col1__lte = val)

- Filtering by column greater than val ---> Book.objects.get(col2__gt = val)

- Filtering by column greater than or equal to val ---> Book.objects.get(col1__gte = val)

- Like Operator (string case sensitive) ---> Book.objects.get(col__contains = val)

- Like Operator (string case insensitive) ---> Book.objects.get(col__icontains = val)



# Or Condition:

- from django.db.models import Q
- OR Condition :  Book.objects.filter(Q(rating__lt = 5) | Q(is_bestselling = True)) 
- OR Condition AND Condition:  Book.objects.filter(Q(rating__lt = 5) | Q(is_bestselling = True), Q(author = 'JK Rowling'))



# References:

- https://docs.djangoproject.com/en/5.1/topics/db/queries/#top
- 