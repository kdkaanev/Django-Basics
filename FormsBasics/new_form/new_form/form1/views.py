from django.http import HttpResponse
from django.shortcuts import render
from new_form.form1.form import EmployeeForm

# Create your views here.
def index(request):
    context = {
        "employee_form": EmployeeForm
    }
    return render(request, 'form1/index.html', context)