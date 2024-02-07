from django import forms
from django.forms import modelform_factory

from forms.new.models import Person


class ReadonlyFieldsMixin:
    read_only_fields = []

    def _mark_readonly_fields(self):
        for field in self.read_only_fields:
            self.fields[field].widget.attrs["readonly"] = True
        # for _,field in self.fields.items():
        #     field.widget.attrs["readonly"] = True


class PersonForm(forms.ModelForm):



    class Meta:
        model = Person
        exclude = ['created_by']

        def __init__(self, *args, **kwargs):
            if 'user' in kwargs:
                self.user = kwargs.pop('user')
            super().__init__(*args, **kwargs)


        labels = {
            'name': 'Name',
        }

        error_messages = {
            'name': {
                'required': 'Name is required',
                'unique': 'Name must be unique',
                'min_length': 'Name must be at least 3 characters',
            }
        }
        def clean(self, *args, **kwargs):
            cleaned_data = super().clean()
            print(cleaned_data)

        def clean_name(self):
            pass

        def save(self, *args, **kwargs):
            instance = super().save(commit=False)
            if self.user.is_authenticated:
                instance.created_by = self.user
            instance.save()
            return instance



PersonForm2 = modelform_factory(Person, fields='__all__')


class PersonForm3(ReadonlyFieldsMixin, PersonForm):
    read_only_fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mark_readonly_fields()

        # self.fields['age'].widget.attrs["readonly"] = True
