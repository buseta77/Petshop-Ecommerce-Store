from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from petstore.models.customer import Customer
from petstore.models.products import Products
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            cart = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        return render(request, 'login.html', {'cart_products': cart_products})

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

        #####

        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        checkout = request.POST.get('checkout')
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if checkout:
                    return redirect('checkout')
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Hatalı email veya şifre!'
        else:
            error_message = 'Hatalı email veya şifre!'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('/login')
