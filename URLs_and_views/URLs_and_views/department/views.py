from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request,*args,**kwargs):
    context = {
        "title":'Request',
        "kwargs": kwargs,
        "path":request.path,
        "method":request.method,
        "user":request.user
    }
    return render(request,'index.html',context)

def index2(request, *args, **kwargs):
    return HttpResponse(f"new huj{args}, {kwargs}")

def department_1_details(request):
    return HttpResponse("dep1")
def department_2_details(request):
    return HttpResponse("dep2")


def department_details(request,pk):
    global department_name
    if pk == 1:
      department_name = 'Dev'
    elif pk == 2:
        department_name = 'Train'
    html_out = "<html><body><h1>" \
    "Department Name: %s, Department ID: %s" \
    "</h1></body></html>" \
    % (department_name, pk)
    return HttpResponse(html_out)


def department_by_name(request,name):
    return HttpResponse(f"display name {name}")

def redirect_to_softuni(request):
    return redirect("https://softuni.bg/")

def redirect_toindex_no_params(request):
    return redirect("/index")


def redirect_whit_params(request):
    return redirect("department_details", pk=12)
