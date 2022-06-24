
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

from main_app.models import Divisions

# Define the home view
def home(request):
  return HttpResponse('<h1>Valley Futbol Club</h1>')

def about(request):
  return render(request, 'about.html')

def divisions_index(request): 
  return render (request, 'divisions/index.html' , {'divisions': Divisions})