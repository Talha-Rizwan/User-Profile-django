'''All forms for base application.'''
from django import forms

from .models import User

# pylint: disable = too-few-public-methods
class UserSignUPForm(forms.ModelForm):
    '''This class deals with user signp/registration'''
    re_enter_password = forms.CharField(label='Re Enter Password', widget=forms.PasswordInput)

    class Meta:
        '''User Signup form.'''
        model = User
        fields = ('email', 'username', 'password', 're_enter_password', 'phone_number', 'address', 'gender', 'profile_pic')
        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }

# pylint: disable=too-few-public-methods
class UserProfileUpdateForm(forms.ModelForm):
    '''This class deals with user profile attributes updation excluding password.'''
    class Meta:
        '''User profile updation form'''
        model = User
        fields = ('username', 'phone_number', 'address', 'gender', 'profile_pic')

# pylint: disable = too-few-public-methods
class ChangePasswordForm(forms.ModelForm):
    '''This class deals with user password updation.'''
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        '''User password updation form'''
        model = User
        fields = []
