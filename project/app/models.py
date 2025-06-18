from django.db import models
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    genre = models.CharField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class BorrowRecord(models.Model):
    user_name=models.CharField()
    book =models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date =models.DateField()
    return_date =models.DateField(blank=True)


