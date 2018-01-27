from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
