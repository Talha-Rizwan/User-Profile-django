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

class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput)

    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)
    again_new_password = forms.CharField(label="ReEnter New Password", widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = []  