from django.contrib import admin
from django.urls import path,include,re_path
from BackGround.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('index/', index),
    path('logout/', logout),
    path('goods_list/', goods_list),
    path('personal_info/', personal_info),
    path('addarticle/',addarticle),
    path('articlelist/',articlelist),
    path('getarticle/',getarticle),
    re_path('getarticle/(?P<id>\d+)',getarticle),


]
