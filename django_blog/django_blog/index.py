import imp
import re
from django.contrib.auth.forms import UserCreationForm
from blog.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def firstPage(request):
    return render(request, 'mainpage.html')

def revPage(request):
    return render(request, 'reviews.html')

def applePage(request):
    return render(request, 'apple.html')

def xiaomiPage(request):
    return render(request, 'xiaomi.html')

def sonyPage(request):
    return render(request, 'sony.html')

def regPage(request):
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account has been created successfully!')
            return redirect('firstPage')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'profile.html')
    