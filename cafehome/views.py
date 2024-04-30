from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Transaction, Computer, Customer
from .forms import AddComputer


class Home(TemplateView, LoginRequiredMixin):
    template_name = "dashboard.html"

    def get_context_data(self):
        if self.request.user.is_authenticated:
            transactions = Transaction.objects.filter(customer_id=self.request.user.id)
            context = {"transactions": transactions}
            return context
        return super().get_context_data()


class Profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self):
        context = {"user": self.request.user}
        return context


class Computer(ListView):
    template_name = "computer.html"
    model = Computer
    context_object_name = "computers"
    
class AddComputer(FormView):
    template_name = "addcomputer.html"
    form_class = AddComputer
    success_url = "/computers"
    
    def form_valid(self, form):
        form.save()        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)


class Transactions(ListView):
    template_name = "transactions.html"
    model = Transaction
    context_object_name = "transactions"


class Users(ListView):
    template_name = "users.html"
    model = Customer
    context_object_name = "customers"


class Staff(ListView):
    template_name = "staff.html"
    model = Customer
    context_object_name = "customers"


class ToggleStatusStaff(View):

    def post(self, request):
        user = Customer.objects.get(id=request.POST["customer_id"])
        user.is_staff = not user.is_staff
        user.save()
        return redirect("staff")
