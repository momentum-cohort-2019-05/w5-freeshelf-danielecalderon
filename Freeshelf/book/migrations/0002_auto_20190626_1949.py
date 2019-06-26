# Generated by Django 2.2.2 on 2019-06-26 19:49

from django.db import migrations
from django.conf import settings
import os
import csv


def load_data(apps, schema_editor):
    Book = apps.get_model('book', 'Book')
    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = Book(title=row['title'], author=row['author'], url=row['url'], 
            description=row['description'])
            book.save()

def space():
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [ migrations.RunPython(load_data,space),
    ]
    
