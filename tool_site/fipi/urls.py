from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('fipi/fipi', views.fipi, name='fipi'),

]