from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def school(request):
    return render(request,"school.html")

def college(request):
    return render(request,"college.html")

def pg(request):
    return render(request,"pg.html")

def ug(request):
    return render(request,"ug.html")

# Create your views here.
