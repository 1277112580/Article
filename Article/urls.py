from django.contrib import admin
from django.urls import path,re_path
from Article.views import *

urlpatterns = [
    path('index/',index),
    path('listpic/', listpic),
    path('about/',about),
    path('newslistpic/',newslistpic),
    re_path('newslistpic/(?P<page>\d+)',newslistpic),
    re_path('articledetails/(?P<id>\d+)',articledetails),
    path('base/',base),
]
