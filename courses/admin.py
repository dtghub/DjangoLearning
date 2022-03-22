from django.contrib import admin
from courses.models import Course_type, Course

admin.site.register(Course_type)
admin.site.register(Course)

