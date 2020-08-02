from django.conf.urls import url
from three import views

urlpatterns=[
    url('getgrade/',views.get_grade),
    url('getstudents/',views.get_students),
]
