from pickle import APPENDS
from django import apps
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return HttpResponse('<h1>welcome<h1>')

def check(request):
    return HttpResponse("<p>python framework<p>")

def use(request):
    return render(request,'app/form.html')

def wait(request):
    return render(request,'app/table.html')

def won(request):
    return render(request,'app/list.html')


def  first(request):
    var='django'
    dic={'var_name':var,"a":"python"}
    return render(request,"app/first.html",context=dic)


def index(request):
    courses = ["C", "C++", "JAVA", "PYTHON", "HTML", "CSS"]
    return render(request, 'app/index1.html', {'name': 'tamil', 'courses': courses})


# def tml(request):
#     courses=["C","C++","JAVA","PYTHON","HTML","CSS"]
#     return render(request,"app/index2.html",context={"users":courses})


def total(request):
    view_users=[
        {"subject":"tamil","mark":98},
        {"subject":"eng","mark":76},
        {"subject":"Maths","mark":98},
        {"subject":"Science","mark":98},
        {"subject":"Social","mark":89},
    ]
    return render(request,"app/index2.html",context={"users":view_users})

