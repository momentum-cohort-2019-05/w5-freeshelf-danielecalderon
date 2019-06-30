from django.shortcuts import render
from .models import Book
from django.views import generic


def index(request):

    book_list = Book.objects.all()
    num_books = Book.objects.all().count()

    context = { 'book_list': book_list,
                'num_books': num_books
    }
    return render(request, 'index.html' , context=context)


class BookListView(generic.ListView):
    model = Book

    def list_books(self):
        return Book.objects.all()
