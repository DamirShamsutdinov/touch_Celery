# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render

from users.forms import CustomUserForm
from users.models import CustomUser
from users.tasks import send_spam_email


def home(request):
    """Домашняя страница со всеми контактами"""
    users = CustomUser.objects.all()
    return render(request, 'users/home.html', {'users': users})


def create(request):
    """Создание объекта-Контакта"""
    error = ''
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            send_spam_email.delay(form.instance.email)
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
