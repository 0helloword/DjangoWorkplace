from django.http import HttpResponse
from django.shortcuts import render
from three.models import Student, Grade


def get_grade(request):
    student=Student.objects.get(pk=1)
    grade=student.s_grade
    return HttpResponse('Grade %s' % grade.g_name)

def get_students(request):
    grade=Grade.objects.get(pk=1)
    students=grade.student_set.all()
    context={
        'students':students,
    }
    return render(request,'getstudents.html',context=context)