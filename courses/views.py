from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Here we have a test'}
    return render(request, 'courses/index.html', context=context_dict)

