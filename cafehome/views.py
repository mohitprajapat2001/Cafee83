# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import View, ListView, FormView, UpdateView
from .models import Transaction, Computer, Customer
from django.db.models import F
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

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Transactions(ListView):
    template_name = constant.TRANSACTION_HTML
    model = Transaction
    context_object_name = "transactions"


class Users(ListView):
    template_name = constant.USER_HTML
    model = Customer
    context_object_name = "customers"


class Staff(ListView):
    template_name = constant.STAFF_HTML
    model = Customer
    context_object_name = "customers"


class ToggleStatusStaff(View):

    def post(self, request):
        user = Customer.objects.get(id=request.POST["customer_id"])
        user.is_staff = not user.is_staff
        user.save(update_fields=["is_staff"])
        return redirect("staff")
