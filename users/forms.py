from django.forms import *
from .models import Customer


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
            widgets[field] = input_option(
                attrs={"class": "form-control"}
            )
