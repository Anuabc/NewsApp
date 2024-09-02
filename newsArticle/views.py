from django.shortcuts import render, redirect

# Create your views here.
def article(request, news):
    return redirect('home')