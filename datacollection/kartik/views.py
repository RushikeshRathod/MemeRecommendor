# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template.loader import get_template
from django.conf.urls.static import static
from .models import meme
import csv
import os
import random
def index_kartik(request):
    all_meme_objects= meme.objects.all()
    temp=meme()
    for item in all_meme_objects:
        if item.field_2==0:
            temp=item
    template = get_template("index.html")
    list_1=[]
    for i in range(0,20):
        temp=[]
        base="http://bighome.iitb.ac.in/~150110029/memes/"
        extension=random.randint(1,150)
        temp.append(extension)
        url_1=base+str(extension)+".png"
        temp.append(url_1)
        list_1.append(temp)
    context={
        'all_meme_objects': all_meme_objects,
        'random_int':list_1,
    }
    return HttpResponse(template.render(context,request))

def index_add_data_kartik(request):
    import xlrd
    # a= os.getcwd()
    # return HttpResponse(a)
    workbook = xlrd.open_workbook("data.xls")
    sh = workbook.sheet_by_name("Sheet1")
    # print sh.nrows
    # print sh.ncols
    data = sh.cell_value(0, 0)
    # print data
    for row in range(1, 51):
        a = meme()
        a.meme_image = "https://scontent-ams3-1.xx.fbcdn.net/v/t1.0-9/29101767_1717204321680003_2332367017836806144_n.jpg?oh=0b715285a700bdade3a3041190015a4d&oe=5B434890"
        a.meme_no =sh.cell_value(row,0)
        a.field_1 = sh.cell_value(row,1)
        a.field_2 = sh.cell_value(row,2)
       # a.field_3 = sh.cell_value(row,3)
       # a.field_4 = sh.cell_value(row,4)
        a.save()

def update_kartik(request):
    #if request.POST:
     #   return HttpResponse(request.POST)
    #    return HttpResponse()
      #  return HttpResponse((request.POST))
    a_0 = request.POST['meme_no_1']
       # a_1=request.POST.getlist('1')
    a_1 =request.POST['1']
    l=[]
    '''
    l.append(a_0)
    l.append(a_1)
    b_0 = request.POST['meme_no_2']
    b_1 =request.POST['2']
    l.append(b_0)
    l.append(b_1)
    '''
    for i in range(1,21):
        meme_no="meme_no_"+str(i)
        l.append(request.POST[meme_no])
        l.append(request.POST[str(i)])
    with open("out.csv", "a") as f:
        wr = csv.writer(f, delimiter=str(u',').encode('utf-8'))
        wr.writerow(l)
    return redirect(index_kartik)

    all_meme_objects= meme.objects.get(meme_no=a)
   # return HttpResponse(a + " "+str(a_4))
    all_meme_objects.field_2 = 1
    all_meme_objects.field_1 = a_4
    all_meme_objects.save()
    b=os.getcwd
