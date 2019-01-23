from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

import json


import sys
sys.path.insert(0, '/Users/vince/Documents/tools/tool_site/fipi/lib')

from portfolio import *


from django.db import models



def fipi(request):


    my_dict = {'x': ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],'y': [1, 20, 15, 5],}

    js_data = json.dumps(my_dict)

    context = {'js_data': js_data,}

    #myP = Portfolio('/Users/vince/Documents/tools/tool_site/fipi/data/reg.json')

    print('ok ok ok')

    return render(request, 'fipi/fipi.html',context)

