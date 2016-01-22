from django.conf.urls import url
from .views import index, post

app_name = 'mainsite'
urlpatterns = [
    url(r'^$', view=index),
    url(r'^index/$', view=index, name='index'),
    url(r'^post/(?P<post_id>[0-9]+)/$', view=post, name='post'),
]
