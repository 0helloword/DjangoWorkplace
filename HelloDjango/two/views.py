import random
from django.http import HttpResponse
from django.shortcuts import render
from two.models import Student

def home(request):
    return render(request,'home.html')

def add_student(request):
    student=Student()
    student.s_name='summer%d'% random.randrange(100)
    student.s_age=random.randrange(50)
    student.save()
    return HttpResponse('add success %s' % student.s_name)

def get_students(request):
    students=Student.objects.all() #获取表中的全部数据
    for student in students:
        print(student.s_name)
    context={
        "hobby":"reading",
        "students":students,
    }
    # return HttpResponse(student.s_name)
    return render(request,'studentlist.html',context=context)

def update_student(request):
    student=Student.objects.get(pk=5)
    student.s_name='lala'
    student.save()
    return HttpResponse('update student success')

def del_student(request):
    student=Student.objects.get(pk=8)
    student.delete()
    return HttpResponse('delete student success')