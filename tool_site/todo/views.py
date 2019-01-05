from django.shortcuts import render
from django.http import HttpResponse

from . models import Todo

from django.db import models
from datetime import datetime


def blog(request,test):
    return HttpResponse("<h1>Todo Homepage {}. </h1>".format(test))


def index(request):
    #return HttpResponse("<h1>Todo Homepage</h1>")

    #query_results = Todo.objects.all()

    activeTodos = Todo.objects.all().exclude(status='T')

    finishedTodos = Todo.objects.all().filter(status='T').filter(finishDate=datetime.now())

    context = {'activeTodos': activeTodos,
               'finishedTodos' : finishedTodos,}


    return render(request, 'todo/list.html',context)



