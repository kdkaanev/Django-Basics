import datetime

from django.shortcuts import render

# Create your views here.

class Person:
    def __init__(self,first_name,last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
def index(request):
    context = {
        'title': 'Employees',
        "person":{
            "first_name": "John",
            "last_name": "Hujo"
        },
        "person_object":Person("John","Hujo"),
        "ll":[1,2,3,4,5,6,7,8,9],
        "date":datetime.date.today(),
        "ages":[1,2,3,4,5,6,7,8,9],
        "get_params":request.GET,

    }

    return render(request,"employees/index.html", context)

def employees_details(request, pk):
    context = {
        'pk': pk
    }
    return render(request, 'details.html', context)