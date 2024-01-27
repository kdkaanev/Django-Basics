from django import forms

class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=True,
    )
    last_name = forms.CharField(
        max_length=35,
        required=True,
    )
    age = forms.IntegerField(
        required=True,
    )

    interest = forms.ChoiceField(
        choices=(
            ('1', 'Gaming'),
            ('2', 'Reading'),
            ('3', 'Move'),
            ('4', 'Sport'),
        )
    )