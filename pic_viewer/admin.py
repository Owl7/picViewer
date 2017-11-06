# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class PicInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_name']

admin.site.register(PicInfo, PicInfoAdmin)