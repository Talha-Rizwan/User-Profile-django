"""All the url paths for the base application are managed"""
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('signup/', UserSignUpView.as_view(), name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('update/', UpdateUserView.as_view(), name="update"),
    path('update-password/', ChangePasswordView.as_view(), name="update-password"),
    path('profiles/', views.showProfiles , name="profiles"),
    
]
