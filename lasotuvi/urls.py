# -*- coding: utf-8 -*-
"""
(c) 2016 Nguyen Van Dung.
"""
from django.conf.urls import url
from django.http import HttpResponse
import datetime
from src.DiaBan import diaBan
from src.ThienBan import lapThienBan
from src import lstv
import json
import os
from settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
import base64

def app(request):
    now = datetime.datetime.now()
    hoTen = unicode(request.GET.get('hoten'))
    ngaySinh = int(request.GET.get('ngaysinh', now.day))
    thangSinh = int(request.GET.get('thangsinh', now.month))
    namSinh = int(request.GET.get('namsinh', now.year))
    gioiTinh = 1 if request.GET.get('gioitinh') == 'nam' else -1
    gioSinh = int(request.GET.get('giosinh', 1))
    timeZone = int(request.GET.get('muigio', 7))
    duongLich = False if request.GET.get('amlich') == 'on' else True
    db = lstv.lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh, gioSinh,
                        gioiTinh, duongLich, timeZone)
    thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                           gioSinh, gioiTinh, hoTen, db)
    laso = {
        'thienBan': thienBan,
        'thapNhiCung': db.thapNhiCung
    }
    myReturn = (json.dumps(laso, default=lambda o: o.__dict__))
    return HttpResponse(myReturn, content_type="application/json")


def index(request):
    filename = os.path.join(BASE_DIR, "frontend", 'index.html')
    with open(filename, 'r') as indexfile:
        html = indexfile.read()
    return HttpResponse(html)

@csrf_exempt
def upload(request):
    imageFolder = os.path.join(BASE_DIR, 'thuvienlaso')
    try:
        hoTen = request.POST.get('hoten')
        ngaySinh = request.POST.get('ngaysinh')
        thangSinh = request.POST.get('thangsinh')
        namSinh = request.POST.get('namsinh')

        if not hoTen:
            hoTen = 'Noname'

        fileName = '-'.join([hoTen, ngaySinh, thangSinh, namSinh]) + '.jpg'

        fullPath = os.path.join(imageFolder, fileName)

        imagedata = request.POST.get('image').replace('data:image/octet-stream;base64,', '').replace(' ', '+')
        imagedata = base64.b64decode(imagedata)
        with open(fullPath, 'w') as imagefile:
            imagefile.write(imagedata)
        
        currentPath = '/'.join(['http:/', request.META['HTTP_HOST'], 'frontend', fileName])

        myResponse = json.dumps({'error' : False, 'message' : currentPath})
    except:
        myResponse = json.dumps({'error' : True, 'message' : "Không lưu được lá số"})
    
    return HttpResponse(myResponse, content_type="application/json")

urlpatterns = [
    url(r'^api', app),
    url(r'^$', index),
    url(r'^upload', upload)
]
