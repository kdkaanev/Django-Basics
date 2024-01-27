from django.http import HttpResponse
from django.shortcuts import render, redirect
from new_form.form1.form import EmployeeForm

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