from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# views here
from .models import Cart, CartItem
from products.models import Product, Variations

def cart_view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    if the_id:
        cart = Cart.objects.get(id = the_id)
        context = {'cart':cart}
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            new_total += line_total
        request.session['cart_items_count'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
    else:
        empty_message = "Your cart is empty, please keep shoping "
        context = {'empty':True,'empty_message':empty_message}
    template = 'cart/cart_view.html'
    return render(request,template, context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
    except Exception as e:
        return HttpResponseRedirect(reverse('cart'))

    cart_item = CartItem.objects.get(id=id)
    # cart_item.delete()
    cart_item.cart = None
    cart_item.save()
    return HttpResponseRedirect(reverse('cart'))

def add_to_cart(request, slug):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id = the_id)
    try:
        product = Product.objects.get(slug = slug)
    except Product.DoesNotExists:
        pass
    except:
        pass
    product_vars = []
    if request.method == 'POST':
        qty = request.POST['qty']
        if int(qty) >= 0:
            for item in request.POST:
            
                key = item
                val = request.POST[key]
                print(key,val)
                try:
                    v = Variations.objects.get(product = product, category__iexact= key, title__iexact =val)
                    product_vars.append(v)
                except:
                    pass
                    
                    
            
            cart_item = CartItem.objects.create(cart = cart,product=product)   
            if len(product_vars) >0 :   
                cart_item.variations.add(*product_vars)
            cart_item.quantity = qty
            cart_item.save()
            return HttpResponseRedirect(reverse('cart'))
    return HttpResponseRedirect(reverse('cart'))
