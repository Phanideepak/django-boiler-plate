# Update Models

- first_book = Book.objects.all()[0]
- first_book.author = 'JK Rowling'
- first_book.is_bestselling = True
- first_book.save()