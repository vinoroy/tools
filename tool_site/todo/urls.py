from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('todo/taskedit/', views.taskedit, name='taskedit'),
    path('todo/taskedit/<test>', views.taskedit, name='taskedit'),
    #url(r'^$', views.index, name='index'),
    path('todo/list/',views.list, name='list'),
    path('todo/log/',views.log, name='log'),

]