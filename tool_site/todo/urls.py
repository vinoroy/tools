from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('blog/<test>',views.blog,name='blog'),
    url(r'^$', views.index, name='index'),

]