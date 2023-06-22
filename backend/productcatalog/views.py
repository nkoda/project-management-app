from django.http import HttpResponse
from django.shortcuts import render
from .models import JSONProduct


def home(request):
    return HttpResponse("HomePage")

def products(request):
    data = JSONProduct.objects.all
    return HttpResponse(request, 'products/all', {'product':data})