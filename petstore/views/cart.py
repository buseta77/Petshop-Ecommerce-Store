from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from petstore.models.customer import Customer
from django.views import View
from petstore.models.products import Products
from petstore.templatetags.cart import cart_quantity, total_cart_price, price_total


class Cart(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        delete = request.POST.get('delete')
        cart = request.session.get('cart')
        if cart:
            if delete:
                cart[product] = 0
                cart.pop(product)
                request.session['cart'] = cart
                return HttpResponseRedirect(request.path_info)
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
        return render(request, 'cart.html', {'cart_products': cart_products})
