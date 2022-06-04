from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from petstore.models.products import Products, Kedi_Mama, Kedi_Kum, Kedi_Odul, Kedi_Oyuncak, Kedi_Tirmalama, Kedi_Kap,\
    Kopek_Mama, Kopek_Tasma, Kopek_Kap, Kopek_Odul, Kopek_Yatak, Kopek_Oyuncak
from petstore.models.main_category import Main_category
from petstore.models.subscriptions import Subscription
from petstore.models.campaigns import Campaign
from django.views import View
import json


# Create your views here.
class Index(View):
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
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        all_products = None
        main_categories = None
        main_categories = Main_category.get_all_main_categories()
        all_products = Products.get_all_products()
        #####
        products_kedi_mama = Kedi_Mama.get_product_number()
        products_kedi_kum = Kedi_Kum.get_product_number()
        products_kedi_odul = Kedi_Odul.get_product_number()
        products_kedi_oyuncak = Kedi_Oyuncak.get_product_number()
        products_kedi_tirmalama = Kedi_Tirmalama.get_product_number()
        products_kedi_kap = Kedi_Kap.get_product_number()
        products_kopek_mama = Kopek_Mama.get_product_number()
        products_kopek_tasma = Kopek_Tasma.get_product_number()
        products_kopek_odul = Kopek_Odul.get_product_number()
        products_kopek_oyuncak = Kopek_Oyuncak.get_product_number()
        products_kopek_yatak = Kopek_Yatak.get_product_number()
        products_kopek_kap = Kopek_Kap.get_product_number()
        #####
        last_five_cat_products = Products.get_last_five_products(1)
        last_five_dog_products = Products.get_last_five_products(2)
        #####
        last_kedi_mama = Kedi_Mama.objects.last()
        last_kedi_kum = Kedi_Kum.objects.last()
        last_kedi_odul = Kedi_Odul.objects.last()
        last_kedi_oyuncak = Kedi_Oyuncak.objects.last()
        last_kedi_tirmalama = Kedi_Tirmalama.objects.last()
        last_kedi_kap = Kedi_Kap.objects.last()
        last_kopek_mama = Kopek_Mama.objects.last()
        last_kopek_tasma = Kopek_Tasma.objects.last()
        last_kopek_odul = Kopek_Odul.objects.last()
        last_kopek_oyuncak = Kopek_Oyuncak.objects.last()
        last_kopek_yatak = Kopek_Yatak.objects.last()
        last_kopek_kap = Kopek_Kap.objects.last()
        #####
        all_campaigns = Campaign.get_campaigns()
        cat_campaigns = Campaign.get_campaigns_by_type('kedi')
        dog_campaigns = Campaign.get_campaigns_by_type('köpek')
        #####
        data = {}
        data['products'] = all_products
        data['main_categories'] = main_categories
        data['products_no_kedi_mama'] = products_kedi_mama
        data['products_no_kedi_kum'] = products_kedi_kum
        data['products_no_kedi_odul'] = products_kedi_odul
        data['products_no_kedi_oyuncak'] = products_kedi_oyuncak
        data['products_no_kedi_tirmalama'] = products_kedi_tirmalama
        data['products_no_kedi_kap'] = products_kedi_kap
        data['products_no_kopek_mama'] = products_kopek_mama
        data['products_no_kopek_tasma'] = products_kopek_tasma
        data['products_no_kopek_odul'] = products_kopek_odul
        data['products_no_kopek_oyuncak'] = products_kopek_oyuncak
        data['products_no_kopek_yatak'] = products_kopek_yatak
        data['products_no_kopek_kap'] = products_kopek_kap
        #####
        data['last_five_cat_products'] = last_five_cat_products
        data['last_five_dog_products'] = last_five_dog_products
        #####
        data['last_kedi_mama'] = last_kedi_mama
        data['last_kedi_kum'] = last_kedi_kum
        data['last_kedi_odul'] = last_kedi_odul
        data['last_kedi_oyuncak'] = last_kedi_oyuncak
        data['last_kedi_tirmalama'] = last_kedi_tirmalama
        data['last_kedi_kap'] = last_kedi_kap
        data['last_kopek_mama'] = last_kopek_mama
        data['last_kopek_tasma'] = last_kopek_tasma
        data['last_kopek_odul'] = last_kopek_odul
        data['last_kopek_oyuncak'] = last_kopek_oyuncak
        data['last_kopek_yatak'] = last_kopek_yatak
        data['last_kopek_kap'] = last_kopek_kap
        #####
        data['all_campaigns'] = all_campaigns
        data['cat_campaigns'] = cat_campaigns
        data['dog_campaigns'] = dog_campaigns
        print('you are: ', request.session.get('email'))
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        data['cart_products'] = cart_products
        return render(request, 'home.html', data)


class AboutUs(View):
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
        return redirect('about-us')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        return render(request, 'about-us.html', {'cart_products': cart_products})


class ContactUs(View):
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
        return redirect('contact-us')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        return render(request, 'contact-us.html', {'cart_products': cart_products})


class Subscribe(View):
    def post(self, request):
        email = request.POST.get('email')
        new_subscriber = Subscription(email=email)
        if email:
            new_subscriber.placeSubscriber()

        return HttpResponse(
            json.dumps({'result': 'success'}),
            content_type="application/json")


def decrease(request):
    if request.method == 'POST':
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

        return HttpResponse(
            json.dumps({'result': 'success'}),
            content_type="application/json")


def increase(request):
    if request.method == 'POST':
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

        return HttpResponse(
            json.dumps({'result': 'success'}),
            content_type="application/json")


def addToCart(request):
    if request.method == 'POST':
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
        newCount = len(cart.keys())

        return HttpResponse(
            json.dumps({'result': 'success', 'newCount': newCount}),
            content_type="application/json")
