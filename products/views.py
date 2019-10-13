from django.shortcuts import render, Http404
from .models import Product
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

