# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PicInfoManager(models.Manager):
    pass

class PicInfo(models.Model):
    # 图片名称
    p_name = models.CharField(max_length=50)
    # 图片添加时间
    p_add_date = models.DateTimeField()
    # 图片最后一次浏览时间
    p_last_view_date = models.DateTimeField()
    # 图片个数，带有反斜杠需要处理
    p_num = models.CharField(max_length=4)
    # 图片点赞个数
    p_like_number = models.IntegerField()
    # 收藏
    p_collection = models.BooleanField()
    # 图片标签
    p_tag = models.CharField(max_length=200)
    # 图片颜色标签
    p_color_tag = models.CharField(max_length=100)
    # 第一张图片地址
    p_first_link = models.CharField(max_length=100)
    # 所有图片
    p_links = models.CharField(max_length=2000)
    # 浏览数
    p_look_num = models.IntegerField()
    # 大分类
    p_big_tag = models.CharField(max_length=10)

    # class Meta:  # 按时间下降排序
    #     ordering = ['-p_add_date']
