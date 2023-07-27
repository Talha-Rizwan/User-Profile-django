from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('signup/', views.userSignUp, name = "signup"),
    path('login/', views.userLogin, name = "login"),
    path('logout/', views.userLogout, name = "logout"),
    path('update/', views.updateUser, name = "update"),
    path('update-password/', views.change_password, name = "updatePassword"),
]