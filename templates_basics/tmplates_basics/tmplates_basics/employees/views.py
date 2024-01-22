from django.shortcuts import render

# Create your views here.

class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
def index(request):
    context = {
        'title': 'Employees',
        "person":{
            "first_name": "John",
            "last_name": "Hujo"
        },
        "person_object":Person("John","Hujo"),
    }

    return render(request,"employees/index.html", context)