from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('fipi/table/', views.table, name='table'),
    path('fipi/fipi/', views.fipi, name='fipi'),
    path('fipi/fipi/<str:portfolioName>/<str:grafType>/',views.fipi, name='fipi'),
    path('fipi/test/', views.test, name='test'),

]