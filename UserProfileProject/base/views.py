from django.shortcuts import render, redirect
from .forms import UserSignUPForm, UserProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def userSignUp(request):
    if request.method == 'POST':
        form = UserSignUPForm(request.POST)
        if form.is_valid() and request.POST.get('password') == request.POST.get('password2'):
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.status='Unverified'
            user.save()
            print("successfully reqistered")
            return redirect('home') 
        else:
            print('password donot match') 
    else:
        form = UserSignUPForm()
   
    return render(request, 'base/signup.html', {'form': form})

def userLogout(request):
    logout(request)
    return redirect('login') 

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            print('user doesnot exist')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('username or password is not correct')
            return redirect('login')


    context = {}
    return render(request, 'base/login.html', context)

def updateUser(request):
    user = request.user
    form = UserProfileUpdateForm(instance=user)

    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}

    return render(request, 'base/update.html', context)
