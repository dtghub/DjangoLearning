from unicodedata import name
from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
]