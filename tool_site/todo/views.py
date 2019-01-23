from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from . models import Todo

from django.db import models
from datetime import datetime, timedelta


from .forms import TodoForm




def list(request):

    activeTodos = Todo.objects.all().exclude(status='T')

    finishedTodos = Todo.objects.all().filter(status='T').filter(upDate=datetime.now())


    print (finishedTodos.count())

    context = {'activeTodos': activeTodos,
               'finishedTodos' : finishedTodos,}


    return render(request, 'todo/list.html',context)



def completed(request,periode,type,title):


    #finishedTodos = Todo.objects.all().filter(status='T')


    if type == 'T':

        if periode == 999:

            finishedTodos = Todo.objects.all().filter(status='T')

        else :

            finishedTodos = Todo.objects.all().filter(status='T').filter(upDate__gt=datetime.now()-timedelta(days=int(periode)))

    elif type == 'Exercice':

        #finishedTodos = Todo.objects.all().filter(status='T')

        #finishedTodos = Todo.objects.all().filter(status='T').filter(upDate__gt=datetime.now() - timedelta(days=int(periode))).filter(category='Pers - Exercice')


        if periode == 999:
            finishedTodos = Todo.objects.all().filter(category__name="Exercice").filter(status='T')


        else :

            finishedTodos = Todo.objects.all().filter(category__name="Exercice").filter(status='T').filter(upDate__gt=datetime.now()-timedelta(days=int(periode)))




    context = {'finishedTodos': finishedTodos,'periode':periode, 'type':type,'title':title,}

    return render(request, 'todo/completed.html',context)


def taskedit(request,test=None):

    submitted = False

    if test != None:

        task = get_object_or_404(Todo, id=test)

    else:

        task = None


    if request.method == 'POST':

        #if task != None:
        form = TodoForm(request.POST, instance=task)
        #else:
        #    form = TodoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('list')


    else:

        form = TodoForm(instance=task)
        #form = TodoForm()

    if 'submitted' in request.GET:
        submitted = True



    result = str(test)

    return render(request, 'todo/taskedit.html',{'form': form, 'page_list': Todo.objects.all(),'submitted': submitted,'result':result})






