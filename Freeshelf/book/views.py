from django.shortcuts import render
from .models import Book
def index(request):
    
    books = Book.objects.all()
    
    response = render(request, 'index.html', {
        'books': books,
         
    })

    return response

def book_detail(request,):
    book = Book.objects.get()
    return render(request, 'books/book_detail.html', {
        'book': book,
    })