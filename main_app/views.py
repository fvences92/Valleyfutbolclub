
from django.shortcuts import render
from main_app.models import Divisions

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def divisions_index(request): 
  return render (request, 'divisions/index.html' , {'divisions': Divisions})