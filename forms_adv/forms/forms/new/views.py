from django.shortcuts import render

from forms.new.form import PersonForm, PersonForm2, PersonForm3
from forms.new.models import Person


# Create your views here.
def index(request):
    context = {
        'person_form': PersonForm,
        'person_form2': PersonForm2,
        'person_form3': PersonForm3,
        'person_list': Person.objects.all(),
    }
    return render(request, 'new/index.html',context)


def create_person(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()

    return index(request)

def show_formset(request):
    form_set = PersonForm2()
    context = {
        'form_set': form_set
    }
    return render(request, 'new/formset.html', context)