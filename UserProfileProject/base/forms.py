from .models import User
from django import forms

class UserSignUPForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }


