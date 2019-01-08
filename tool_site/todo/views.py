from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from . models import Todo

from django.db import models
from datetime import datetime


from .forms import TodoForm




def list(request):

    activeTodos = Todo.objects.all().exclude(status='T')

    finishedTodos = Todo.objects.all().filter(status='T').filter(upDate=datetime.now())


    print (finishedTodos.count())

    context = {'activeTodos': activeTodos,
               'finishedTodos' : finishedTodos,}


    return render(request, 'todo/list.html',context)



def log(request):

    return HttpResponse("<h2>Test log</h2>")


def taskedit(request,test):

    submitted = False

    task = get_object_or_404(Todo, id=test)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=task)

        if form.is_valid():

            form.save()

            return redirect('list')


    else:
        form = TodoForm(instance=task)

    if 'submitted' in request.GET:
        submitted = True



    result = str(test)

    return render(request, 'todo/taskedit.html',{'form': form, 'page_list': Todo.objects.all(),'submitted': submitted,'result':result})






