from django.shortcuts import (render,
                            Http404,
                            HttpResponseRedirect,
                            redirect,)
from django.urls import reverse
from django.contrib import messages
from .models import Product, ProductImage
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context = {'products': Product.objects.all}
    template = 'products/home.html'
    return render(request, template, context)

def all(request):
    context = {'products': Product.objects.all}
    template = 'products/all.html'
    return render(request, template, context)
def single(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        images = product.productimage_set.all()
        context = {'product': product,
                    'images':images}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404
    return render(request, template, context)
def search(request):
    try:
        query = request.GET.get('q')
    except:
        query = None
    if query:
        products = Product.objects.filter(title__icontains = query)
        context = {'query': query,'products':products}
        template = 'products/results.html'
    else:
        context = {}
        template = 'products/all.html'
    
    return render(request, template, context)
def create_product(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to be logged in to add products.")
        return redirect('auth_login')
    print('sk1')
    product_form = forms.ProductForm(request.POST or None)
    product_image_form = forms.ProductImageForm(request.POST, request.FILES)
    if product_form.is_valid():
        print('sk2')
        new_product = product_form.save(commit=False)
        new_product.save()
        if product_image_form.is_valid():
            product_image = product_image_form.save(commit=False)
            product_image.product = new_product
            product_image.save()
        else:
            messages.error(request,'Something went wrong your product has not been added')
            redirect('single')
        print('sk4')
        messages.success(request, "Your product have been added.")
        return redirect('single-product',slug = new_product.slug)
    
    context = {'product_form': product_form,
                'product_image_form': product_image_form,
                }
    return render(request,'products/create_product.html',context)
        
            





