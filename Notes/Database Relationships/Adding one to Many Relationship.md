# Adding one to many relationships.

- Create Entity Book, Author in models.py file.
- Add author field to Book entity.
    - author = models.ForeignKey(Author, on_delete = models.CASCADE)