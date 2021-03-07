from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about1(request):
    return render(request, 'about.html')

def contact1(request):
    return render(request, 'contact.html')

def tours1(request):
    return render(request, 'tours.html')