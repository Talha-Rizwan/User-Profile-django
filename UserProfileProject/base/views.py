"""All views for the base application."""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView, FormView
from django.urls import reverse_lazy
from django.views.generic import ListView

from .models import User
from .forms import UserSignUPForm, UserProfileUpdateForm, ChangePasswordForm

@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    """The main page in the application"""

    def get(self, request):
        """Method to deal with rendering logic """
        return render(request, 'base/home.html')

class UserSignUpView(FormView):
    """Renders and handles the new user signup form."""
    template_name = 'base/signup.html'
    form_class = UserSignUPForm
    success_url = 'home' 

    def form_valid(self, form):
        if form.cleaned_data['password'] == form.cleaned_data['re_enter_password']:
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.status = 'Unverified'
            user.save()
            print("Successfully registered")
            return redirect(self.success_url)
        print('Passwords do not match')
        return self.render_to_response(self.get_context_data(form = form))

@method_decorator(login_required(login_url='login'), name='dispatch')
class UserLogoutView(View):
    """Renders and handles the user logout."""
    def get(self, request):
        """Method calls the logout user funciton. """
        logout(request)
        return redirect('login')

def user_login(request):
    """renders and handle the user login form"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            print('user doesnot exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        print('username or password is not correct')
        return redirect('login')
    return render(request, 'base/login.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateUserView(UpdateView):
    """Renders and handles the update user profile attributes form logic"""
    template_name = 'base/update.html'
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(FormView):
    """Renders and handles the user account change password logic."""
    template_name = 'base/updatePassword.html'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        user = authenticate(
            self.request,
            email=self.request.user,
            password=form.cleaned_data['old_password']
        )

        if user is not None:
            if form.cleaned_data['new_password'] == form.cleaned_data['confirm_password']:
                new_password = form.cleaned_data['new_password']
                user.set_password(new_password)
                user.save()
                print('Password updated successfully!')
                return redirect('login')
            print("New password values do not match!")
        else:
            print('Incorrect old password')
        return render(self.request, self.template_name, {'form': form})

class ShowProfilesView(ListView):
    model = User
    template_name = 'base/profiles.html'
    context_object_name = 'profiles'