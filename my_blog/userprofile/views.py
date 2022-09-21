import django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("Error in username or password, please try again.")
        else:
            return HttpResponse("Ilegal username or password, please try again.")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("Please use GET or POST to acquire data.")

def user_logout(request):
    logout(request)
    return redirect("article:article_list")

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # Set Password
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # Save data, login, then retern to artical list.
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("Error in user register form, please try again.")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("Please use GET or POST to acquire data.")

@login_required(login_url="/userprofile/login/")
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        # Make sure the logged in user and user to delete is the same
        if request.user == user:
            # log out, delete data, and return to the article list.
            logout(request)
            user.delete()
            return redirect("article:article_list")
        else:
            return HttpResponse("You do not have the permission to delete.")
    else:
        return HttpResponse("Only accept POST requests.")