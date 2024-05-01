from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm, LoginForm
from .models import Customer

# Create your views here.

class Register(FormView):
    template_name = "html/registration/register.html"
    form_class = CustomerForm
    success_url = '/home'
    
    def form_valid(self, form):
        user = form.save(commit=False) 
        user.set_password(form.cleaned_data["password"]) 
        user.save() 
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
        
class Login(FormView):
    template_name = "html/registration/login.html"
    form_class = LoginForm
    success_url = '/home'
    
    def form_valid(self, form):
        user = Customer.objects.get(username=form.cleaned_data["username"])
        if user.check_password(form.cleaned_data["password"]):
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(self.request, user)
                return super().form_valid(form)
        else:
            form.add_error(None, "Incorrect username or password.")
            return super().form_invalid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
class Logout(View):
    
    def get(self, request):
        print("logout")
        logout(request)
        return redirect("/home")