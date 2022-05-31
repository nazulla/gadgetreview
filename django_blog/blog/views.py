from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainpage.html')

def signup(request):
    return render(request, 'signup.html')
