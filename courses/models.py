from datetime import date
from turtle import title
from django.db import models
from django.utils import timezone

class Course_type(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    Course_type=models.ForeignKey(Course_type, on_delete=models.CASCADE)
    title=models.CharField(max_length=128)
    starting_date=models.DateField(default=date.today)
    course_description=models.CharField(max_length=512)

    def __str__(self):
        return self.title
    
