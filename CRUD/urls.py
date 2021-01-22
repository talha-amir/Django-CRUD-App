# from django.shortcuts import redirect
from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('display', views.student_dispay,name='student_display'),
    path('del', views.student_delete,name='student_delete'),
    path('form', views.student_form,name='student_form'),
    path('delete/<str:roll_number>', views.student_delete,name='student_delete'),

    path('form/<str:roll_number>', views.student_form,name='student_update'),

]




