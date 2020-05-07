from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('posts/', views.posts),
    path('allposts/', views.all_posts),
    path('about/', views.about),
    path('details/<int:id>/', views.details),
    # url(r'^/details/(?P<id>\d+)/$', views.details, name='details')
]