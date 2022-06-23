
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Valley Futbol Club</h1>')

def about(request):
  return render(request, 'about.html')

def players_index(request): 
  return render (request, 'players/index.html' , {'players': players})