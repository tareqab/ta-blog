from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    #/blog
    url(r'^$', views.post_list, name = 'post_list'),
    #/blog/post_id
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_detail'),
    #/blog/post_id/share
    url(r'^(?P<post_id>[0-9]+)/share/$', views.post_share, name = 'post_share')
]
