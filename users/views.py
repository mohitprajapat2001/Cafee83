# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import View, FormView
from django.contrib.auth import authenticate, login, logout
from login_required import login_not_required
from .forms import CustomerForm, LoginForm
from cafee83 import constant


@login_not_required
class Register(FormView):
    template_name = constant.REGISTER_HTML
    form_class = CustomerForm
    success_url = constant.LOGIN_URL

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super().form_valid(form)


@login_not_required
class Login(FormView):
    template_name = constant.LOGIN_HTML
    form_class = LoginForm
    success_url = constant.HOME_URL

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            form.add_error(None, "Incorrect username or password.")
            return super().form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect("/home")
