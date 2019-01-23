from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404



def index(request):

    #return HttpResponse('<h1>This is the index site</h1>')

    return render(request, 'index.html')