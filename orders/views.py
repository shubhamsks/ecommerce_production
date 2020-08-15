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
import stripe
# import stripe 

# stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
def orders(request):
	context = {'orders': Order.objects.all()}
	template = 'orders/myorders.html'
	return render(request, template, context)

# request user login
@login_required
def checkout(request):
	try:
		address_added = request.GET.get('address_added')
	except:
		address_added = None
	if address_added is not None:
		address_form = None
	else:
		address_form = UserAdressForm()
	current_addresses = UserAdress.objects.filter(user=request.user)
	context = {
		'address_form': address_form,
		'current_addresses': current_addresses,
		'stripe_key' : settings.STRIPE_PUBLISHABLE_KEY
		}
	template = 'orders/checkout.html'	

	return render(request, template, context)

@login_required
def charge(request):
	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id = the_id)
	except:
		the_id = None
		return HttpResponseRedirect(reverse('cart'))
	try:
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.final_total = 1
		new_order.save()
	except:
		return HttpResponseRedirect(reverse('cart'))
	if request.method == 'POST':
		new_order.status = 'Finished'
		print(new_order.status)
		new_order.save()
		if new_order.status == 'Finished':
			del request.session['cart_id']
			del request.session['cart_items_count']
		charge = stripe.Charge.create(
			amount=100,
			currency='inr',
			description='Some Order',
			source=request.POST['stripeToken']
		)
		return render(request,'orders/charge.html')
def coming_soon(request):
	return render(request,'coming_soon.html',{})


