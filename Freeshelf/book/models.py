from django.db import models
from django.urls import reverse

BOOK_CATAGORY = (
    ('python', 'Python'),
    ('ruby', 'Ruby'),
    ('javascript', "Javascript"),)

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Catagory(models.Model):
    catagory = models.CharField(max_length=200) 

    def __str__(self):
        return self.title


