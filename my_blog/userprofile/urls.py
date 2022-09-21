from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # User log in
    path('login/', views.user_login, name='login'),
    # User log out
    path('logout/', views.user_logout, name='logout'),
    # Create new user
    path('register/', views.user_register, name='register'),
    # Delete user
    path('delete/<int:id>/', views.user_delete, name='delete'),
]