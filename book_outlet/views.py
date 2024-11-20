from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg, Count 
import math

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('rating')
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))

    return render(request, 'book_outlet/index.html', {
        'books' : books,
        'total_number_of_books' : num_books,
        'average_rating' : avg_rating['rating__avg']
    })

def book_detail(request, slug):
    book = get_object_or_404(Book.objects.filter(slug = slug))
    return render(request, 'book_outlet/book_detail.html', {'book' : book})
