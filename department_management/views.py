from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Department


def department_list(request):
    departments = Department.objects.all().order_by('department_name')
    return render(request, 'department_management/index.html', {'departments': departments})


def department_create(request):
    if request.method == 'POST':
        department_code = request.POST.get('department_code')
        department_name = request.POST.get('department_name')
        department_head = request.POST.get('department_head')
        office_location = request.POST.get('office_location')
        date_established = request.POST.get('date_established')

        if department_code and department_name and department_head and office_location and date_established:
            Department.objects.create(
                department_code=department_code,
                department_name=department_name,
                department_head=department_head,
                office_location=office_location,
                date_established=date_established,
            )
            return redirect('department_list')

    return render(request, 'department_management/create.html')


def department_edit(request, id):
    department = get_object_or_404(Department, id=id)

    if request.method == 'POST':
        department.department_code = request.POST.get('department_code')
        department.department_name = request.POST.get('department_name')
        department.department_head = request.POST.get('department_head')
        department.office_location = request.POST.get('office_location')
        department.date_established = request.POST.get('date_established')
        department.save()
        return redirect('department_list')

    return render(request, 'department_management/edit.html', {'department': department})


def department_delete(request, id):
    department = get_object_or_404(Department, id=id)

    if request.method == 'POST':
        department.delete()
        return redirect('department_list')

    return render(request, 'department_management/delete.html', {'department': department})
