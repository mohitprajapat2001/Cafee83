from django.shortcuts import render, HttpResponse
from django.views.generic import *
from .models import Computer

# Create your views here.

# def home(request):
#     return render(request, "base.html")

class Home(TemplateView):
    template_name = "dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = {"name":"Mohit"}
        return context
    
class Computer(ListView):
    template_name = "computer.html"
    model = Computer
    context_object_name = "computers"
    
