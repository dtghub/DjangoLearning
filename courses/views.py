from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course

def index(request):
















    context_dict = {'boldmessage': 'Here we have a test'}
    return render(request, 'courses/index.html', context=context_dict)

