from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth import authenticate, login
from .forms import CustomerForm, LoginForm

# Create your views here.

class Profile(TemplateView):
    template_name = "profile.html"
    
class Register(FormView):
    template_name = "register.html"
    form_class = CustomerForm
    success_url = '/login'
    
    def form_valid(self, form):
        user = form.save(commit=False) 
        user.set_password(form.cleaned_data["password"])  # Set the password for the user
        user.save() 
        user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
        
class Login(FormView):
    template_name = "login.html"
    form_class = LoginForm
    
class Logout(TemplateView):
    template_name = "logout.html"