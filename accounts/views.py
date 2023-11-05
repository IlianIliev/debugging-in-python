from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render, redirect

from accounts.forms import UserForm
from accounts.models import User


def accounts(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "users": User.objects.all()
    }
    return render(request, 'accounts.html', context)


def create(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/accounts')

    context = {
        "form": form,
    }
    return render(request, 'create.html', context)


def delete(request, user_id):
    if request.POST:
        User.objects.filter(id=user_id).delete()
        return redirect('/accounts')

    context = {
        'user': User.objects.filter(id=user_id).first()
    }
    return render(request, 'delete.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('/')

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
