from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='indexview'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post, name='post'),
]