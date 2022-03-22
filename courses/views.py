from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course

def index(request):
    course_list=Course.objects.order_by('title')
    context_dict = {}
    context_dict = course_list
    return render(request, 'courses/index.html', context=context_dict)

