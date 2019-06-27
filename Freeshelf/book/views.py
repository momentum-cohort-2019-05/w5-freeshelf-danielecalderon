from django.shortcuts import render
from .models import Book


def index(request):
    book_list = Book.objects.all()
    
    context = { 'book_list': book_list
    }
    return render(request, 'index.html' , context=context)

# def book_detail(request,):
#     book = Book.objects.get()
#     return render(request, 'books/book_detail.html', {
#         'book': book,
#     })