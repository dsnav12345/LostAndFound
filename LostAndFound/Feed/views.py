from django.shortcuts import render, redirect
from .models import Post,ImageSearchModel
from .forms import PostForm,ImageSearchForm
from django.contrib import messages
import speech_recognition as sr
# Create your views here.
from django.http import HttpResponse
import subprocess
from pathlib import Path
import sys
import os
import colordescriptor,index1,search1,searcher
from index1 import indexpy
BASE_DIR = Path(__file__).resolve().parent.parent
categorytypes = [
    "mobiles",
    "watches",
    "mobileaccessories",
    "laptops",
    "speakers",
    "camera",
    "footwear",
    "winterWear",
    "waterBottle",
    "bag",
    "books",
    "cycle",
    "bankingitems",
    "diaries",
    "calculators",
    "spectacles",
    "keys",
    "purse",
]


def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts' : posts})

def postitem(request):
    if request.user.is_authenticated:
        if request.method == 'POST' :
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                print('post saved')
                post = form.save()
                post.user = request.user
                post.save()
            return redirect("/home")
        else :
            form = PostForm()
            return render(request, 'postitem.html', {'form': form})
    else:
        messages.info(request, 'please login to post an item')
        return redirect("/accounts/login")

def postdetails(request, postid):
    post = Post.objects.get(id=postid)
    return render(request, 'postdetails.html', {'post':post})
def imgsearch(request):
    if(request.method =='POST'):
        uploadedfiles=ImageSearchForm(request.POST,request.FILES)
        if uploadedfiles.is_valid():
            uf=uploadedfiles.save()
            print("uploading the given files")
            print(uf.id)
            obj=ImageSearchModel.objects.get(id=uf.id)
            print(obj.imgtosearch.url)
            global queryimg
            queryimg=obj.imgtosearch.url
            list1=list(queryimg)
            list1[1]='M'
            queryimg=''.join(list1)
            list2=list(str(BASE_DIR))
            list3=list2+list1
            print("Printing list 3")
            queryimg=''.join(list3)
            print(queryimg)

        return redirect("/imgsearchresults")
    else:
        im=ImageSearchForm()
        return render(request, 'imgsearch.html',{"imgsearch":im})
def imgsearchresults(request):
    #index1.indexpy("laf","secondindex.csv")
    print('query img is',queryimg)
    count=8123
    name='data{}.csv'.format(count)
    print(count)
    urlarray=search1.search(name,queryimg,'jpg')
    print(urlarray)
    return render(request,'imgsearchresults.html',{"result":urlarray})
def extractfeatures(request):
        global count
        count=8123
        name='data{}.csv'.format(count)
        indexpy('jpg',name)
        return HttpResponse("Exctraction complete",name)
def category(request,categorytype):
    posts = Post.objects.filter(category=categorytype)
    return render(request, 'category.html', {'posts' : posts})

def voicesearch(request):
        text='Oops could not recognize'
        s=sr.Recognizer()
        with sr.Microphone() as source:
            audio=s.listen(source)
            try:
                text=s.recognize_google(audio)
                print(s.recognize_google(audio))
                text=text.lower()
                if text in categorytypes:
                    redi='category/{}'.format(text)
                    return redirect(redi)

            except:
                print('Could not convert sorry')
        return render(request,'voicesearch.html',{"voice":text})