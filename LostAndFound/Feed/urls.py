from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home' , views.home, name='home'),
    path('<int:postid>', views.postdetails, name='postdetails'),
    path('postitem', views.postitem, name='postitem'),
    path('imgsearch',views.imgsearch, name='imgsearch'),
    path('imgsearchresults',views.imgsearchresults, name='imgsearchresults'),
    path('extractfeatures',views.extractfeatures, name='extractfeatures'),
    path('category/<categorytype>',views.category, name='categories'),
    path('voicesearch', views.voicesearch, name="voicesearch"),
]
