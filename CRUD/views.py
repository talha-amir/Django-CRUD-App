from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import templates
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    print("Request Object :" , request.content_type)
    # return HttpResponse("<h1>Hello World</h1>")
    response = redirect("/display")
    return response

def student_dispay(request):
    context = {'student_data':Student.objects.all()}
    return render(request,'CRUD/display.html',context)

# Will be used for insert and update 
def student_form(request,roll_number = None):
    form = StudentForm

    if request.method == 'GET':
        if roll_number is  not None:
            student = Student.objects.get(pk=roll_number)
            form = StudentForm(instance=student)
        
        return render(request,'CRUD/form.html',{'form':form})
    else:
        if roll_number is None:
            form = form(request.POST)
        else:
            student = Student.objects.get(pk=roll_number)
            form = StudentForm(request.POST,instance= student)

        if form.is_valid():
            form.save()
        return redirect('/display')

def student_delete(request,roll_number = None):

    student = Student.objects.get(pk=roll_number)
    student.delete()
    return redirect('/display')
