from django.shortcuts import render, HttpResponseRedirect
from cart.models import Cart
from django.urls import reverse
from .models import Order
import time
from .utils import id_generator
from django.contrib.auth.decorators import login_required
from accounts.forms import UserAdressForm
from accounts.models import UserAdress
from django.conf import settings
# import stripe 

# stripe.api_key = settings.STRIPE_SECRET_KEY
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
		new_order = Order.objects.get(cart=cart)
		print('here ',new_order.order_id)
	except Order.DoesNotExist:
		print('here2')
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		print('cart total',cart.total)
		new_order.save()
	except:
		print('reversing')
		return HttpResponseRedirect(reverse('cart'))
	try:
		address_added = request.GET.get('address_added')
		print('address',address_added)
	except:
		address_added = None
	if address_added is not None:
		address_form = None
	else:
		address_form = UserAdressForm()
	current_addresses = UserAdress.objects.filter(user=request.user)
	if request.method == 'POST':
		payment_card = request.POST.get('payment_card')
		exp_month = request.POST.get('exp_month')
		exp_year = request.POST.get('exp_year')
		cvc = request.POST.get('cvc')
	if new_order.status == 'Finished':
		del request.session['cart_id']
		del request.session['cart_items_count']
	context = {'address_form': address_form,
				'current_addresses':current_addresses,}
	template = 'orders/checkout.html'	

	return render(request, template, context)
# @login_required
# def stripe_payment_view(request):
# 	address = request.POST.get('address', "")
# 	print(type(address))
# 	print(address)
# 	context = {}
# 	template = "orders/stripe.html"
# 	return render(request, template, context)
def coming_soon(request):
	return render(request,'coming_soon.html',{})