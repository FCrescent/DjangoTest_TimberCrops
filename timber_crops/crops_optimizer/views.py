from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, TimberCrops!")

def home(request):
    return render(request, 'home.html')

def settings_hub(request):
    return render(request, 'settings_hub.html')