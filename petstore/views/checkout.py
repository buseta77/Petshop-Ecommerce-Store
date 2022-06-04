from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from petstore.models.customer import Customer
from django.views import View
from petstore.models.products import Products
from petstore.models.orders import OrderGuest, OrderCustomer, OrderProduct
from petstore.templatetags.cart import cart_quantity, total_cart_price, price_total
import random


class CheckOut(View):
	def post(self, request):
		cart = request.session.get('cart')
		if 'null' in list(cart.keys()):
			del cart['null']
		products = Products.get_products_by_id(list(cart.keys()))
		charge = float(total_cart_price(products, cart))
		cargo = 100
		note = request.POST.get('note')

		city = request.POST.get('city')
		district = request.POST.get('district')
		neighborhood = request.POST.get('neighborhood')
		address = request.POST.get('address')
		order_no = random.randint(10000, 1000000)

		customer = request.session.get('customer')
		if customer is None:
			name = request.POST.get('firstname')
			surname = request.POST.get('lastname')
			phone = request.POST.get('phone')
			email = request.POST.get('email')
			order = OrderGuest(order_no=order_no, city=city, district=district, neighborhood=neighborhood,
							address=address, charge=charge, cargo=cargo, note=note, first_name=name, last_name=surname,
							phone=phone, email=email)
			error_message = self.validateGuestCustomer(order)
			if not error_message:
				order.placeOrder()
			else:
				ids = list(request.session.get('cart').keys())
				cart_products = Products.get_products_by_id(ids)
				return render(request, 'checkout.html', {'cart_products': cart_products, 'message': error_message})
		else:
			order = OrderCustomer(order_no=order_no, city=city, district=district, neighborhood=neighborhood, address=address,
								charge=charge, cargo=cargo, note=note, customer=Customer(id=customer))
			error_message = self.validateSignedCustomer(order)
			if not error_message:
				order.placeOrder()
			else:
				ids = list(request.session.get('cart').keys())
				cart_products = Products.get_products_by_id(ids)
				return render(request, 'checkout.html', {'cart_products': cart_products, 'message': error_message})
		for product in products:
			quantity = cart_quantity(product, cart)
			item_instance = OrderProduct(order=order, product=product, solo_price=product.price, quantity=quantity)
			item_instance.register()

		request.session['cart'] = {}
		ordered_products = OrderProduct.get_items_by_order(order)
		return render(request, 'success.html', {'order': order, 'ordered': ordered_products})

	def get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		if 'null' in list(cart.keys()):
			del cart['null']
		ids = list(request.session.get('cart').keys())
		cart_products = Products.get_products_by_id(ids)
		return render(request, 'checkout.html', {'cart_products': cart_products})

	def validateGuestCustomer(self, order):
		error_message = None
		if not order.city:
			error_message = "Şehrinizi girin!"
		elif not order.district:
			error_message = 'İlçenizi girin!'
		elif not order.neighborhood:
			error_message = 'Mahallenizi girin!'
		elif not order.address:
			error_message = 'Adres satırını girin!'
		if not order.first_name:
			error_message = "İsminizi girin!"
		elif len(order.first_name) < 2:
			error_message = 'İsim bir karakterden fazla olmalı!'
		elif not order.last_name:
			error_message = 'Soyisminizi girin!'
		elif len(order.last_name) < 2:
			error_message = 'Soyisim bir karakterden fazla olmalı!'
		elif not order.phone:
			error_message = 'Telefonunuzu girin!'
		elif len(order.phone) < 10:
			error_message = 'Telefon numarası en az on karakter olmalı!'
		elif len(order.email) < 7:
			error_message = 'Email en az yedi karakterden oluşmalı!'
		return error_message

	def validateSignedCustomer(self, order):
		error_message = None
		if not order.city:
			error_message = "Şehrinizi girin!"
		elif not order.district:
			error_message = 'İlçenizi girin!'
		elif not order.neighborhood:
			error_message = 'Mahallenizi girin!'
		elif not order.address:
			error_message = 'Adres satırını girin!'
		return error_message
