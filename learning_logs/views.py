from django.shortcuts import render
from django.http import HttpResponse
from.models import Topic
# Create your views here.
def home(request):
    """The home page for Learning Log"""
    return render(request, 'index.html')

def topics(request):
    """Show all topics."""

    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}
    
    return render(request, 'topics.html', context)