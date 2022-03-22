from datetime import date
from turtle import title
from django.db import models
from django.utils import timezone
class Course(models.Model):
    title=models.CharField(unique=True, max_length=128)
    starting_date=models.DateField(default=date.today)
    course_description=models.CharField(max_length=512)

    def __str__(self):
        return self.title
    
