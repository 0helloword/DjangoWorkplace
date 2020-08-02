from django.conf.urls import url
from two import views

urlpatterns=[
    url('home/',views.home),
    url('addstudent/',views.add_student),
    url('getstudents/',views.get_students),
    url('updatestudent/',views.update_student),
    url('delstudent/',views.del_student),
]