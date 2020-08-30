from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    time_start=models.TimeField()
    time_end=models.TimeField()
    bookings=models.IntegerField()

class ticket(models.Model):
    movie=models.CharField(max_length=200)
    book_time=models.TimeField()
    user=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    nos=models.IntegerField()