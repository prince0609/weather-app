from django.test import TestCase
import requests
# Create your tests here.

response = requests.get(f"http://api.weatherstack.com/current?access_key=8572fbbb824bc227cfe269c44579db0a&query=mumbai")
# context = {'response':response}

print(response.reason)