from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import *

# Import Required ClassView
from .models import Transaction, Computer, Customer
from .forms import ComputerForm
from users.forms import UserUpdateForm


class Home(ListView):
    template_name = "html/cafeehtml/dashboard.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return self.request.user.transaction_set.all()


class Profile(UpdateView):
    model = Customer
    form_class = UserUpdateForm
    template_name = "html/cafeehtml/Profile.html"
    
    def get_success_url(self):
        return f"/home/profile/{self.request.user.pk}"


class Computer(ListView):
    template_name = "html/cafeehtml/computer.html"
    model = Computer
    context_object_name = "computers"


class ComputerForm(FormView):
    template_name = "html/cafeehtml/computerform.html"
    form_class = ComputerForm
    success_url = "/home/computers"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Transactions(ListView):
    template_name = "html/cafeehtml/transactions.html"
    model = Transaction
    context_object_name = "transactions"


class Users(ListView):
    template_name = "html/cafeehtml/users.html"
    model = Customer
    context_object_name = "customers"


class Staff(ListView):
    template_name = "html/cafeehtml/staff.html"
    model = Customer
    context_object_name = "customers"


class ToggleStatusStaff(View):

    def post(self, request):
        user = Customer.objects.get(id=request.POST["customer_id"])
        user.is_staff = not user.is_staff
        user.save()
        return redirect("staff")
