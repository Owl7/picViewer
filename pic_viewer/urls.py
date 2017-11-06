from django.conf.urls import url
from pic_viewer import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.index),
    url(r'^meixiong$', views.meixiong),
    url(r'^qiaotun$', views.qiaotun),
    url(r'^siwa$', views.siwa),
    url(r'^neiyi$', views.neiyi),
    url(r'^rihan$', views.rihan),
    url(r'^om$', views.om),
    url(r'^qingchun$', views.qingchun),
    url(r'^zhifu$', views.zhifu),
    url(r'^pic_viewer/(\d+)', views.pic_detail),
]