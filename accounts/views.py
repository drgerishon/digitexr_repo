from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required, permission_required


def success_page(request):
    return render(request, 'test.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out....')
    return redirect('index')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Successfully Logged In')
            return redirect('index')

        else:
            messages.success(request, 'Error Logging In - Try again....')
            return redirect('accounts:login')
    else:

        return render(request, 'accounts/login.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Successfully Registered. Please Login to Proceed')
            return redirect('accounts:login')

    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Successfully Updated Your Profile')
            return redirect('index')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You Have Successfully Updated Your Password')
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
