from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import UpdateStudent, CreateStudent
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    students = Student.objects.all()
    pagination = Paginator(students, 4)
    page = request.GET.get('page')
    students = pagination.get_page(page)
    context = {'students': students}
    return render(request, 'school_app/home.htm', context)


def view_std(request, pk):
    students = Student.objects.get(id=pk)
    context = {'students': students}
    return render(request, 'school_app/student.htm', context)


def techer(request):
    emp = Employee.objects.all()
    pagination = Paginator(emp, 3)
    page = request.GET.get('page')
    emp = pagination.get_page(page)
    context = {'emp': emp}
    return render(request, 'school_app/teacher.htm', context)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        students = Student.objects.filter(f_name=q)
        context = {'query': q, 'students': students}
        template = 'school_app/result.htm'
    else:
        template = 'school_app/home.htm'
        context = {}
    return render(request, template, context)


def update_std(request, pk):
    students = Student.objects.get(id=pk)
    form = UpdateStudent(instance=students)
    if request.method == 'POST':
        form = UpdateStudent(request.POST, request.FILES, instance=students)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'students': students}
    return render(request, 'school_app/update.htm', context)


def create_std(request):
    students = Student.objects.all()
    form = CreateStudent()
    if request.method == 'POST':
        form = CreateStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'school_app/new_student.htm', context)
