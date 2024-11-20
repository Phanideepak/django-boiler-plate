# Aggregation and Ordering

books = Book.objects.all()

- count : books.count()
- Avg : books.aggregate(Avg(rating))

- Order By ASC : books.order_by('col')
- Order By DESC:  books.order_by('-col')