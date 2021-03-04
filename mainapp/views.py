from django.shortcuts import render


def homepage(request, ):
    return render(request, 'mainapp/index.html')


def products(request, ):
    return render(request, 'mainapp/products.html')
# Create your views here.
