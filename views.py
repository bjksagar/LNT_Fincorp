from django.db import models
from rest_framework import serializers

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    class Meta:
        db_table="book"


