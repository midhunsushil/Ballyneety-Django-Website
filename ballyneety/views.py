from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request, "index.html")

def about_us(request):

    return render(request, "about_us.html")

def mares(request):

    return render(request, "mares.html")

def stallions(request):

    return render(request, 'stallions.html')

def progeny(request):

    return render(request, 'progeny.html')

def for_sale(request):

    return render(request, 'for_sale.html')

def contact_us(request):

    return render(request, 'contact_us.html')
