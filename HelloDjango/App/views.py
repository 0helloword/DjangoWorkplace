from django.http import HttpResponse
from django.shortcuts import render


def haha(request):
    return HttpResponse('这是一个测试网页')

def index(request):
    return render(request,'index.html') #读取模板文件

def home(request):
    return render(request,'home.html')