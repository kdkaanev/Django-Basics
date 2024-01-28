from django.http import HttpResponse
from django.shortcuts import render, redirect
from new_form.form1.form import EmployeeForm, EmployeeNormalForm
from new_form.form1.models import Employee


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            return redirect('index')
    context = {'form': form,}
    return render(request, 'form1/index.html', {'form': form})





def index_models(request):
    form = EmployeeNormalForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index_models')
    context = {
        "normal_form": EmployeeNormalForm(),
        "employee_form": EmployeeForm(),
        "show_employee": Employee.objects.all()
    }
    return render(request, 'form1/index_models.html', context)

def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'GET':
        form = EmployeeNormalForm(instance=employee)
    else:
        form = EmployeeNormalForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index_models')
    context = {
        'form': form,
        'employee': employee
    }

    return render(request, 'form1/update_employee.html', context)
