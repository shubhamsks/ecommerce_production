from django.shortcuts import render, HttpResponseRedirect
from cart.models import Cart
from django.urls import reverse
from .models import Order
import time
from .utils import id_generator
from django.contrib.auth.decorators import login_required
# Create your views here.
def orders(request):
	context = {}
	template = 'orders/user.html'
	return render(request, template, context)

# request user login
@login_required
def checkout(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id = the_id)
	except:
		the_id = None
		return HttpResponseRedirect(reverse('cart'))

	try:
		new_order = Order.objects.get(cart = cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()
	except:
		# some error message 
		return HttpResponseRedirect(reverse('cart'))
	if new_order.status == 'Finished':
		del request.session['cart_id']
		del request.session['cart_items_count']
	context = {}
	template = 'products/home.html'

	return render(request, template, context)