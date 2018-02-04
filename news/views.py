from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article


def index(request):
    article_list = Article.objects.order_by('-created_at')
    context = {'article_list' : article_list}
    return render(request, 'news/home.html', context)

def about(request):
    return render(request, 'news/about.html')

def categories(request):
    return render(request, 'news/categories.html')

def privacy(request):
    return render(request, 'news/privacy.html')

def post(request, slug):
    return render(request, 'news/posttemplate.html', {'article': get_object_or_404(Article, slug=slug)})
