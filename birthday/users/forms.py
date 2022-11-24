# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateInput, EmailInput
from django.shortcuts import redirect

from users.models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birthday', 'email']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first_name'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'last_name'
            }),
            "birthday": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'birthday YYYY-MM-DD'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            })
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        if CustomUser.objects.filter(first_name=cleaned_data['first_name'],
                                     last_name=cleaned_data['last_name'],
                                     birthday=cleaned_data['birthday']
                                     ).exists():
            raise ValidationError(
                'CustomUser with this data is already exists'
            )
        return cleaned_data
