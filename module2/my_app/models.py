from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30)

    description = models.TextField(null = True, blank = True)

    published_date = models.DateField(null = True, blank = True)

    def __str__(self):

        return f'Book Title: {self.title}, Author: {self.author}, published in {self.published_date}'

    def get_bookID(self):
        return f'The Id of the book is {self.id}'
    
    