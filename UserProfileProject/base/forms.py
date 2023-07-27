from .models import User
from django import forms

class UserSignUPForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number', 'address', 'gender')
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'address', 'gender')