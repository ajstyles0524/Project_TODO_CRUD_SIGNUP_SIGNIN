from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from employee_crud.forms import EmployeeForm
from employee_crud.models import Employee


# Create your views here.
def index(request):
    return HttpResponse("Hello GAGA")


# Create your views here.
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'temp.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(E_id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(E_id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(E_id=id)
    employee.delete()
    return redirect("/show")
