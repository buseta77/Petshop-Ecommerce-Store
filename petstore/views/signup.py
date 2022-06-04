from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from petstore.models.customer import Customer
from petstore.models.products import Products
from django.views import View


class Signup(View):
	def get(self, request):
		cart = request.session.get('cart')
		if not cart:
			request.session['cart'] = {}
		if 'null' in list(cart.keys()):
			del cart['null']
		ids = list(request.session.get('cart').keys())
		cart_products = Products.get_products_by_id(ids)
		return render(request, 'signup.html', {'cart_products': cart_products})

	def post(self, request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		if not product is None:
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

		#######

		postData = request.POST
		first_name = postData.get('firstname')
		last_name = postData.get('lastname')
		phone = postData.get('phone')
		email = postData.get('email')
		password = postData.get('password')
		# validation
		value = {
			'first_name': first_name,
			'last_name': last_name,
			'phone': phone,
			'email': email
		}
		error_message = None

		customer = Customer(first_name=first_name,
							last_name=last_name,
							phone=phone,
							email=email,
							password=password)
		error_message = self.validateCustomer(customer)

		if not error_message:
			print(first_name, last_name, phone, email, password)
			customer.password = make_password(customer.password)
			customer.register()
			return redirect('login')
		else:
			data = {
				'error': error_message,
				'values': value
			}
			return render(request, 'signup.html', data)

	def validateCustomer(self, customer):
		error_message = None
		if not customer.first_name:
			error_message = "İsminizi girin"
		elif len(customer.first_name) < 2:
			error_message = 'İsim bir karakterden fazla olmalı!'
		elif not customer.last_name:
			error_message = 'Soyisminizi girin'
		elif len(customer.last_name) < 2:
			error_message = 'Soyisim bir karakterden fazla olmalı!'
		elif not customer.phone:
			error_message = 'Telefonunuzu girin'
		elif len(customer.phone) < 10:
			error_message = 'Telefon numarası en az on karakter olmalı!'
		elif len(customer.password) < 5:
			error_message = 'Şifre en az beş karakterden oluşmalı!'
		elif len(customer.email) < 7:
			error_message = 'Email en az yedi karakterden oluşmalı!'
		elif customer.isExists():
			error_message = 'Böyle bir email adresi zaten var'
		# saving

		return error_message
