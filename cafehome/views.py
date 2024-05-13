# -*- coding: utf-8 -*-
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group
from django.views.generic import View, ListView, FormView, UpdateView, TemplateView
from .models import Transaction, Computer, Customer
from .forms import ComputerForm
from users.forms import UserUpdateForm
from cafee83 import constant


class Home(ListView):
    template_name = constant.DASHBOARD_HTML
    context_object_name = "customers"

    def get_queryset(self):
        return self.request.user.transactions.all()


class Profile(UpdateView):
    template_name = constant.PROFILE_HTML
    model = Customer
    form_class = UserUpdateForm

    def get_success_url(self):
        return f"/home/profile/{self.request.user.pk}"


class Computer(ListView):
    template_name = constant.COMPUTER_HTML
    model = Computer
    context_object_name = "computers"


class ComputerForm(FormView):
    template_name = constant.COMPUTERFORM_HTML
    form_class = ComputerForm
    success_url = constant.COMPUTER_URL

    def dispatch(self, request):
        if not request.user.groups.filter(name=constant.COMPUTER_EDITOR).exists():
            return PermissionRequired.as_view()(request)
        return super().dispatch(request)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Transactions(ListView):
    template_name = constant.TRANSACTION_HTML
    model = Transaction
    context_object_name = "transactions"
    ordering = "-created"


class Users(ListView):
    template_name = constant.USER_HTML
    model = Customer
    context_object_name = "customers"

    def dispatch(self, request):
        if (
            request.user.groups.filter(name=constant.USER_VIEWER).exists()
            or request.user.is_superuser
        ):
            return super().dispatch(request)
        return PermissionRequired.as_view()(request)


class Groups(ListView):
    template_name = constant.GROUPS_HTML
    model = Customer
    context_object_name = "customers"
    ordering = "id"

    def dispatch(self, request):
        if not request.user.is_superuser:
            return PermissionRequired.as_view()(request)
        return super().dispatch(request)


class Info(TemplateView):
    template_name = constant.INFO_HTML


class UserGroupEdit(View):

    def dispatch(self, request):
        if not request.user.is_superuser:
            return PermissionRequired.as_view()(request)
        return super().dispatch(request)

    def post(self, request):
        group_names = request.POST.getlist("groupSelect")
        user = Customer.objects.get(id=request.POST.get("customer_id"))
        user.groups.clear()
        groups = Group.objects.filter(name__in=group_names)
        user.groups.add(*groups)
        return redirect("/home/groups")


class PermissionRequired(TemplateView):
    template_name = constant.PERMISSION_REQUIRED_HTML


def error_404(request, exception):
    return render(request, constant.ERROR_HTML_404, status=404)


def error_500(request):
    return render(request, constant.ERROR_HTML_500, status=500)
