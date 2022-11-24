# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from users.forms import CustomUserForm
from users.models import CustomUser


def home(request):
    users = CustomUser.objects.all()
    return render(request, 'users/home.html', {'users': users})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:home')
        else:
            error = 'Форма заполнена неверно, ' \
                    'либо пользователь уже существует. ' \
                    'Попробуйте еще раз!'

    form = CustomUserForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'users/signup.html', data)


def success(request):
    return render(request, 'users/success.html')
