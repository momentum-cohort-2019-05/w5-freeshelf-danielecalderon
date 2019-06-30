from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Catagory(models.Model):
    catagory = models.CharField(max_length=200) 

    def __str__(self):
        return self.catagory
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for a book category."""
        return reverse('category-detail', args=[str(self.id)])


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200, unique=True)
    description = models.TextField(max_length=1000) 
    date_added = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self

    class Meta:
        ordering = ['date_added']
    

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('index')


    # , args=[str(self.id)]
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # book_author = models.ForeignKey('BookAuthor', on_delete=models.SET_NULL, null=True)
    
    # ManyToManyField used because category can contain many books. Books can belong to multiple categories.
    # book_category = models.ManyToManyField(Category, help_text='Select categories for this book')

    
    



    # class Meta:
    #     """Plural name for category to override category+s"""
    #     verbose_name_plural = "categories"

    
    
    
  
   


    
         
   









