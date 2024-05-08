# -*- coding: utf-8 -*-
from django.forms import (
    Form,
    ModelForm,
    TextInput,
    CharField,
    PasswordInput,
    FileInput,
    NumberInput,
    SelectMultiple,
)
from .models import Customer
from django.contrib.auth.models import Group


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "username", "email", "password"]
        widgets = {}
        for field in fields:
            widgets[field] = TextInput(
                attrs={"class": "form-control", "required": "True"}
            )


class LoginForm(Form):
    username = CharField(
        required=True, max_length=30, widget=TextInput(attrs={"class": "form-control"})
    )
    password = CharField(
        required=True, widget=PasswordInput(attrs={"class": "form-control"})
    )


class UserUpdateForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["profile", "first_name", "last_name", "age", "phone", "address"]
        widgets = {}
        for field in fields:
            if field == "profile":
                input_option = FileInput
            elif field == "age" or field == "phone":
                input_option = NumberInput
            else:
                input_option = TextInput
            widgets[field] = input_option(attrs={"class": "form-control"})


class UpdateUserGroup(ModelForm):
    class Meta:
        model = Customer
        fields = ["groups"]
        widgets = {"groups": SelectMultiple(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields["groups"].queryset = Group.objects.all()
