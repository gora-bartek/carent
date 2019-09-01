from django.shortcuts import render
from .models import Car

def homepage(request):
    return render(request = request,
                  template_name="main/home.html",
                  context={"cars": Car.objects.all})