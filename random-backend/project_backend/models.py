from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
