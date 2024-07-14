from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def mandal(request):
    return HttpResponse('hello')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return render(request,'products.html')
def productDetails(request):
    return render(request,'product-details.html')
def cart(request):
    return render(request,'cart.html')
def account(request):
    return render(request,'account.html')
def about(request):
    return render(request,'about.html')
