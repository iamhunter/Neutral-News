from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.
from .models import Article


def index(request):
    return render(request, 'news/home.html')
    
def post(request, slug):    
    return render(request, 'news/posttemplate.html', {'article': get_object_or_404(Article, slug=slug)})
    
class IndexView(generic.ListView):
    template_name = 'news/home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions. (not including those set to be published in the future)."""
        return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]