from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    page_obj=products=Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name !=' ' and product_name is not None:
        page_obj=products.filter(name__icontains=product_name)


    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={
        'page_obj':page_obj
    }
    return render(request, 'mainapp/index.html',context)  

# @login_required
def add_product(request):
    if request.method == 'POST':
           name=request.POST.get('name')
           price=request.POST.get('price')
           desc=request.POST.get('desc')
           image=request.FILES['upload']
           seller_name = request.user
           product=Product(name=name,price=price,desc=desc,image=image, seller_name= seller_name)
           product.save()
    return render(request,'mainapp/add_product.html')

def update_product(request,id):
    product=Product.objects.get(id=id)
    
    if request.method=='POST':
        product.name=request.POST.get('name')
        product.price=request.POST.get('price')
        product.desc=request.POST.get('desc')
        product.image=request.FILES['upload']
        product.save()
        return redirect('/mainapp/homepage')
    context={
        'product':product,
    }
    return render(request,'mainapp/update_product.html',context)

def delete_product(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product':product,
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/mainapp/homepage')
    
    return render(request,'mainapp/delete_product.html',context)

def my_listings(request):
    product = Product.objects.filter(seller_name=request.user) 
    context = {
        'product':product,
    }
    return render(request,'mainapp/my_ads.html',context)


def product_detail(request,id):
    product=Product.objects.get(id=id)
    context={
        'product' : product
    }
    return render(request, 'mainapp/detail_page.html',context)

def mysell(request):
    product = Product.objects.filter(name=request.user) 
    context = {
        'product':product,
    }
    return render(request,'shopapp/mysell.html',context)

def wishlist(request):
    pass