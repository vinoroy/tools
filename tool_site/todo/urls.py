from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('todo/taskedit/', views.taskedit, name='taskedit'),
    path('todo/taskedit/<test>', views.taskedit, name='taskedit'),
    #url(r'^$', views.index, name='index'),
    path('todo/list/',views.list, name='list'),
    path('todo/completed/<int:periode>/<str:type>/<str:title>',views.completed, name='completed'),
    path('todo/completed/<periode>/',views.completed, name='completed'),
    path('todo/completed/',views.completed, name='completed'),

]