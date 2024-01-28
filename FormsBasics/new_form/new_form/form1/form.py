from django import forms

from new_form.form1.models import Employee


class EmployeeForm(forms.Form):

    first_name = forms.CharField(
        max_length=35,
        required=True,
        label='First Name',
    )
    last_name = forms.CharField(
        max_length=35,
        required=True,
        label='Last Name',
    )
    age = forms.IntegerField(
        required=True,
    )

    role = forms.IntegerField(
        widget=forms.RadioSelect(choices=Employee.ROLES),
        required=True,
    )
class EmployeeNormalForm(forms.ModelForm):


    class Meta:
            model = Employee
            fields = '__all__'


            labels = {
                'first_name': 'First Name',
                'last_name': 'Last Name',
            }
            widgets = {
                'role': forms.RadioSelect(
                    choices=Employee.ROLES,
                    attrs={'required': True},
                ),
            }