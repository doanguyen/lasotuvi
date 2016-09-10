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
    myreturn = (json.dumps(laso, default=lambda o: o.__dict__))
    return HttpResponse(myreturn, content_type="application/json")


def index(request):
    filename = os.path.join(BASE_DIR, "frontend", 'index.html')
    with open(filename, 'r') as indexfile:
        html = indexfile.read()
    return HttpResponse(html)

urlpatterns = [
    url(r'^api', app),
    url(r'^$', index),
]
