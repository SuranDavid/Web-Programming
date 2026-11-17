from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Student, Module

def modulelist(request):
    return render(request, 'myApp/modulelist.html', {'modules': Module.objects.all().order_by('code')})

def home(request):
    return render(request, 'myApp/home.html', {'student_count': Student.objects.count(), 'module_count': Module.objects.count()})
def studentlist(request, page=1):
    students = Student.objects.all().order_by('lastName','firstName')

    paginator = Paginator(students, 10)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)
    return render(request, 'myApp/studentlist.html', {'page_obj': page_obj})
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'myApp/student_detail.html', {'student': student})
