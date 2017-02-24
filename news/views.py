from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'news/home.html')
    
def post(request, slug):
    return render(request, 'news/posttemplate.html')
    return render_to_response('news/posttemplate.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })