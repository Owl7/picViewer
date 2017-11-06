# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from .models import *


def index(request):
    picList = PicInfo.objects.filter(p_big_tag='meixiong').order_by('-p_add_date')
    context = {'picList': picList}

    return render(request, 'home.html', context)

def meixiong(request):
    picList = PicInfo.objects.filter(p_big_tag='meixiong').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)

def qiaotun(request):
    picList = PicInfo.objects.filter(p_big_tag='qiaotun').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)


def qingchun(request):
    picList = PicInfo.objects.filter(p_big_tag='qingchun').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)

def siwa(request):
    picList = PicInfo.objects.filter(p_big_tag='siwa').order_by('-p_add_date')
    context = {'picList': picList}

    return render(request, 'home.html', context)

def neiyi(request):
    picList = PicInfo.objects.filter(p_big_tag='neiyi').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)

def zhifu(request):
    picList = PicInfo.objects.filter(p_big_tag='zhifu').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)


def rihan(request):
    picList = PicInfo.objects.filter(p_big_tag='rihan').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)

def om(request):
    picList = PicInfo.objects.filter(p_big_tag='om').order_by('-p_add_date')
    context = {'picList': picList}
    return render(request, 'home.html', context)


def pic_detail(request, id):
    pic = PicInfo.objects.filter(pk=id)[0]
    context = {'links': pic.p_links.split(','), 'name': pic.p_name}

    # pic.p_look_num += 1
    # PicInfo.objects.filter(pk=id).update(p_look_num=pic.p_look_num)

    return render(request, 'pic_viewer/picDetail.html', context)