from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
            r'(?P<post>[-\w]+)/$',
            views.post_detail,
            name='post_detail'),
    path('new/', views.post_new, name='post_new'),
]
