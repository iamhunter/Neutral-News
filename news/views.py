from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Article


def index(request):
    article_list = Article.objects.all()
    context = {'article_list' : article_list}
    return render(request, 'news/home.html', context)
    
def post(request, slug):    
    return render(request, 'news/posttemplate.html', {'article': get_object_or_404(Article, slug=slug)})