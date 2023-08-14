from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

# def contactus(request):
#     return render(request, 'contact_us.html', {})

class Contactus (TemplateView):
    template_name = 'contact_us.html'
