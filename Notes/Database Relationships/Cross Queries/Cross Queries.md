# Cross Queries

- Take Author and Book Models. Author - Book has one-many relationshops.

- book = Books.objects.filter(author__last_name = 'JK')
  where last_name is field of Model Author.

- Get list of books written by author. 
  author = Author.objects.filter(author__first_name = 'Zoroaster')
  `books = author.book_set.all()` 