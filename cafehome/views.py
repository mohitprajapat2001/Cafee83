from django.shortcuts import render, HttpResponse
from django.views.generic import *
from .models import Computer
from django.contrib.auth import authenticate

# Create your views here.

# def home(request):
#     return render(request, "base.html")

class Home(TemplateView):
    template_name = "dashboard.html"
    
    def get_context_data(self):
        context = {"name":"Mohit"}
        return context
    
class Profile(TemplateView):
    template_name = "profile.html"
    
    def get_context_data(self):
        context = {"user":self.request.user}
        print(self.request.user.id)
        return context
    
    
class Computer(ListView):
    template_name = "computer.html"
    model = Computer
    context_object_name = "computers"
    
