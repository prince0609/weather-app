from django.shortcuts import render, redirect
import requests

# Create your views here.

#weatherstack api
def weather(request):
          response = requests.get(f"http://api.weatherstack.com/current?access_key=8572fbbb824bc227cfe269c44579db0a&query=New York").json()
          context = {'response':response}
          if request.POST.get('search'):
                  search = request.POST.get('search')
                  response = requests.get(f"http://api.weatherstack.com/current?access_key=8572fbbb824bc227cfe269c44579db0a&query={search}").json()
                  context = {'response':response}
                  

          
          return render(request, 'index.html', context=context)