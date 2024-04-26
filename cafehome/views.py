from django.shortcuts import render, HttpResponse
from django.views.generic import *

# Create your views here.

# def home(request):
#     return render(request, "base.html")

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = {"name":"Mohit"}
        return context
        
    
