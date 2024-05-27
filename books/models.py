from django.db import models

class Author(models.Model):
    name = models.CharField(max_lengt=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_lengt=100)

class book(models.Model):
    tittle = models.CharField(max_lengt=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return self.tittle