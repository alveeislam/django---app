from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

