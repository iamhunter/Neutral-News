from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article


def index(request):
    return render(request, 'news/home.html')
    
def post(request, slug):    
    return render(request, 'news/posttemplate.html', {'article': get_object_or_404(Article, slug=slug)})