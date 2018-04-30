import openpyxl
from django.http import Http404 #to include http 404 messages
from django.http import HttpResponse
from django.template import loader
from django.template.backends import django
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from openpyxl import load_workbook
from io import BytesIO
import pandas as pd
import os
import sys
from .models import meme

@csrf_exempt
def default(request):
    '''
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {#whenever you pass info in template you pass it via dictionary
        'all_albums': all_albums,
    }
    template.render(context, request)
    '''
   # temp = '<form action="file" method="POST"><input type="file" name="xlmsfile"><input type="submit"></form>'
#    os.system('python loader.py')
 #   from .models import meme

    a = meme()
    a.meme_image = "https://scontent-ams3-1.xx.fbcdn.net/v/t1.0-9/29101767_1717204321680003_2332367017836806144_n.jpg?oh=0b715285a700bdade3a3041190015a4d&oe=5B434890"
    a.meme_no = 1
    a.field_1 = 2
    a.field_2 = 3
    a.field_3 = 4
    a.field_4 = 5
    a.save()

    x=meme.objects.all()
    y=""
    for temp in x:
      y=y+"  "+str(temp.field_1)
      # y=y+str(temp.field_1)+str(temp.field_2)+" "

    return HttpResponse(y+" "+str(x.count()))

@csrf_exempt
def openxlms(request):
    if request.method == 'POST' and request.POST['xlmsfile']:
        # file = request.POST['xlmsfile']
        # xl_file = pd.ExcelFile(file)
        #
        # dfs = {sheet_name: xl_file.parse(sheet_name)
        #        for sheet_name in xl_file.sheet_names}
        file = request.FILES.get('xlmsfile')
        return HttpResponse(file)
    return HttpResponse('Hello world')
