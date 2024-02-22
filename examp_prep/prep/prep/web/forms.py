
from django import forms

from prep.user_profile.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }


