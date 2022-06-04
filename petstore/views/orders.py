from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password

import petstore.models.orders
from petstore.models.customer import Customer
from django.views import View
from petstore.models.products import Products
from petstore.models.orders import Order, OrderCustomer, OrderProduct, OrderGuest


class OrderView(View):
	def post(self, request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity <= 1:
						cart.pop(product)
					else:
						cart[product] = quantity - 1
				else:
					cart[product] = quantity + 1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1
		request.session['cart'] = cart
		return HttpResponseRedirect(request.path_info)

	def get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		if 'null' in list(cart.keys()):
			del cart['null']
		ids = list(request.session.get('cart').keys())
		cart_products = Products.get_products_by_id(ids)
		customer = request.session.get('customer')
		orders = OrderCustomer.get_orders_by_customer(customer)
		user = Customer.get_customer_by_id(customer)
		return render(request, 'orders.html', {'orders': orders, 'cart_products': cart_products, 'user': user})


class myOrder(View):
	def get(self, request):
		order_no = request.GET.get('order_no')
		try:
			order = Order.objects.get(order_no=order_no)
		except:
			return render(request, 'sorgula.html', {'error': True})
		ordered_products = OrderProduct.get_items_by_order(order)
		return render(request, 'myOrder.html', {'order': order, 'ordered': ordered_products})


class orderSorgula(View):
	def get(self, request):
		return render(request, 'sorgula.html')
