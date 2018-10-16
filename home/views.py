"""Views for Home App - pages that are not connected with core logic for issue tracker"""
from django.shortcuts import render

# Create your views here.
def index(request):
    """Render index page"""
    return render(request, 'index.html')
