from django.views.generic import View
from django.shortcuts import render, HttpResponseRedirect, redirect
from petstore.models.products import Products, Kedi_Mama, Kedi_Kum, Kedi_Odul, Kedi_Oyuncak, Kedi_Tirmalama, Kedi_Kap,\
    Kopek_Mama, Kopek_Tasma, Kopek_Odul, Kopek_Oyuncak, Kopek_Yatak, Kopek_Kap


class ProductList(View):
    def post(self, request, id, brand):
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

    def get(self, request, id, brand):
        if brand == 'all':
            products = Products.objects.filter(main_category=id)
        else:
            products = Products.objects.filter(main_category=id, brand=brand)
        last_instance = Products.objects.filter(main_category=id).last()
        if str(last_instance.main_category) == 'Kedi':
            subcategories = [['Kedi Mamaları', '/kedi-mama/0/0/'],
                             ['Kedi Kumları', '/kedi-kum/0/0/'],
                             ['Kedi Ödülleri', '/kedi-odul/0/0/'],
                             ['Kedi Oyuncakları', '/kedi-oyuncak/0/0/'],
                             ['Kedi Tırmalamaları', '/kedi-tirmalama/0/0/'],
                             ['Kedi Mama Kapları', '/kedi-kap/0/0/']]
        elif str(last_instance.main_category) == 'Köpek':
            subcategories = [['Köpek Mamaları', '/kopek-mama/0/0/'],
                             ['Köpek Tasmaları', '/kopek-tasma/0/0/'],
                             ['Köpek Ödülleri', '/kopek-odul/0/0/'],
                             ['Köpek Oyuncakları', '/kopek-oyuncak/0/0/'],
                             ['Köpek Yatakları', '/kopek-yatak/0/0/'],
                             ['Köpek Mama Kapları', '/kopek-kap/0/0/']]
        else:
            subcategories = []
        shopby = {}
        shopby2 = Products.get_distinct_brands(id)
        tail_name = ''
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath = '/collection/' + str(id) + '/'
        tail = 'all/'
        tail2 = ''
        basepath_brand = ''
        filtrele = 'no'
        category = f'{last_instance.main_category.name} Ürünleri'
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'cart_products': cart_products, 'category': category,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Mama(View):
    def post(self, request, choice, yes_or_no, ingred, brand):
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

    def get(self, request, choice, yes_or_no, ingred, brand):
        last_instance = Kedi_Mama.objects.last()
        category = 'Kedi Mamaları'
        subcategories = [['Kuru Mamalar', '/kedi-mama/1/1/'],
                         ['Yaş Mamalar', '/kedi-mama/1/0/'],
                         ['Yavru Kedi Mamaları', '/kedi-mama/2/1/'],
                         ['Yetişkin Kedi Mamaları', '/kedi-mama/2/0/'],
                         ['Kısır Kedi Mamaları', '/kedi-mama/3/1/']]
        shopby = Kedi_Mama.get_distinct_ingred()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Mama.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Lezzet'
        filtrele = 'yes'
        products = Kedi_Mama.objects.all()
        if brand == 'all':
            if ingred == 'all':
                if choice == 1:
                    products = Kedi_Mama.objects.filter(kuru_or_yas=yes_or_no)
                elif choice == 2:
                    products = Kedi_Mama.objects.filter(yavru_or_yetiskin=yes_or_no)
                elif choice == 3:
                    products = Kedi_Mama.objects.filter(kisir_or_not=yes_or_no)
            else:
                if choice == 1:
                    products = Kedi_Mama.objects.filter(kuru_or_yas=yes_or_no, neyli=ingred)
                elif choice == 2:
                    products = Kedi_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred)
                elif choice == 3:
                    products = Kedi_Mama.objects.filter(kisir_or_not=yes_or_no, neyli=ingred)
                else:
                    products = Kedi_Mama.objects.filter(neyli=ingred)
        else:
            if ingred == 'all':
                if choice == 1:
                    products = Kedi_Mama.objects.filter(kuru_or_yas=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kedi_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, brand=brand)
                elif choice == 3:
                    products = Kedi_Mama.objects.filter(kisir_or_not=yes_or_no, brand=brand)
                else:
                    products = Kedi_Mama.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kedi_Mama.objects.filter(kuru_or_yas=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 2:
                    products = Kedi_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 3:
                    products = Kedi_Mama.objects.filter(kisir_or_not=yes_or_no, neyli=ingred, brand=brand)
                else:
                    products = Kedi_Mama.objects.filter(neyli=ingred, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby, 'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Kum(View):
    def post(self, request, choice, yes_or_no, litre, brand):
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

    def get(self, request, choice, yes_or_no, litre, brand):
        last_instance = Kedi_Kum.objects.last()
        category = 'Kedi Kumları'
        subcategories = [['Silika Kumlar', '/kedi-kum/1/1/'],
                         ['Bentonit Kumlar', '/kedi-kum/1/0/'],
                         ['Topaklanan Kumlar', '/kedi-kum/2/1/'],
                         ['Emici Kumlar', '/kedi-kum/2/0/']]
        shopby = Kedi_Kum.get_distinct_neyli()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Kum.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Ağırlık'
        filtrele = 'yes'
        products = Kedi_Kum.objects.all()
        if brand == 'all':
            if litre == 'all':
                if choice == 1:
                    products = Kedi_Kum.objects.filter(silika_or_bentonit=yes_or_no)
                elif choice == 2:
                    products = Kedi_Kum.objects.filter(topaklanan_or_emici=yes_or_no)
            else:
                if choice == 1:
                    products = Kedi_Kum.objects.filter(silika_or_bentonit=yes_or_no, neyli=litre)
                elif choice == 2:
                    products = Kedi_Kum.objects.filter(topaklanan_or_emici=yes_or_no, neyli=litre)
                else:
                    products = Kedi_Kum.objects.filter(neyli=litre)
        else:
            if litre == 'all':
                if choice == 1:
                    products = Kedi_Kum.objects.filter(silika_or_bentonit=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kedi_Kum.objects.filter(topaklanan_or_emici=yes_or_no, brand=brand)
                else:
                    products = Kedi_Kum.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kedi_Kum.objects.filter(silika_or_bentonit=yes_or_no, neyli=litre, brand=brand)
                elif choice == 2:
                    products = Kedi_Kum.objects.filter(topaklanan_or_emici=yes_or_no, neyli=litre, brand=brand)
                else:
                    products = Kedi_Kum.objects.filter(neyli=litre, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby, 'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Odul(View):
    def post(self, request, choice, yes_or_no, ingred, brand):
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

    def get(self, request, choice, yes_or_no, ingred, brand):
        last_instance = Kedi_Odul.objects.last()
        category = 'Kedi Ödülleri'
        subcategories = [['Kedi Bisküvileri', '/kedi-odul/1/1/'],
                         ['Kedi Stick Ödülleri', '/kedi-odul/1/0/'],
                         ['Yavru Kedi Ödülleri', '/kedi-odul/2/1/'],
                         ['Yetişkin Kedi Ödülleri', '/kedi-odul/2/0/']]
        shopby = Kedi_Odul.get_distinct_neyli()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Odul.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Lezzet'
        filtrele = 'yes'
        products = Kedi_Odul.objects.all()
        if brand == 'all':
            if ingred == 'all':
                if choice == 1:
                    products = Kedi_Odul.objects.filter(biskuvi_or_stick=yes_or_no)
                elif choice == 2:
                    products = Kedi_Odul.objects.filter(yavru_or_yetiskin=yes_or_no)
            else:
                if choice == 1:
                    products = Kedi_Odul.objects.filter(biskuvi_or_stick=yes_or_no, neyli=ingred)
                elif choice == 2:
                    products = Kedi_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred)
                else:
                    products = Kedi_Odul.objects.filter(neyli=ingred)
        else:
            if ingred == 'all':
                if choice == 1:
                    products = Kedi_Odul.objects.filter(biskuvi_or_stick=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kedi_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, brand=brand)
                else:
                    products = Kedi_Odul.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kedi_Odul.objects.filter(biskuvi_or_stick=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 2:
                    products = Kedi_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred, brand=brand)
                else:
                    products = Kedi_Odul.objects.filter(neyli=ingred, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby, 'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Oyuncak(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kedi_Oyuncak.objects.last()
        category = 'Kedi Oyuncakları'
        subcategories = [['Tünel Oyuncaklar', '/kedi-oyuncak/1/3/'],
                         ['Lazerli Oyuncaklar', '/kedi-oyuncak/1/2/'],
                         ['Oltalı Oyuncaklar', '/kedi-oyuncak/1/1/'],
                         ['Peluş Oyuncaklar', '/kedi-oyuncak/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Oyuncak.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kedi_Oyuncak.objects.all()
        if brand == 'all':
            if choice == 1:
                products = Kedi_Oyuncak.objects.filter(oltali_or_pelus=yes_or_no)
        else:
            if choice == 1:
                products = Kedi_Oyuncak.objects.filter(oltali_or_pelus=yes_or_no, brand=brand)
            else:
                products = Kedi_Oyuncak.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Tirmalama(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kedi_Tirmalama.objects.last()
        category = 'Kedi Tırmalamaları'
        subcategories = [['Karton Tırmalamalar', '/kedi-tirmalama/1/1/'],
                         ['Ahşap Tırmalamalar', '/kedi-tirmalama/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Tirmalama.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kedi_Tirmalama.objects.all()
        if brand == 'all':
            if choice == 1:
                products = Kedi_Tirmalama.objects.filter(karton_or_ahsap=yes_or_no)
        else:
            if choice == 1:
                products = Kedi_Tirmalama.objects.filter(karton_or_ahsap=yes_or_no, brand=brand)
            else:
                products = Kedi_Tirmalama.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kedi_Kap(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kedi_Kap.objects.last()
        category = 'Kedi Kapları'
        subcategories = [['Seramik Mama Kapları', '/kedi-kap/1/1/'],
                         ['Plastik Mama Kapları', '/kedi-kap/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kedi_Kap.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kedi_Kap.objects.all()
        if brand == 'all':
            if choice == 1:
                products = Kedi_Kap.objects.filter(seramik_or_plastik=yes_or_no)
        else:
            if choice == 1:
                products = Kedi_Kap.objects.filter(seramik_or_plastik=yes_or_no, brand=brand)
            else:
                products = Kedi_Kap.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Mama(View):
    def post(self, request, choice, yes_or_no, ingred, brand):
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

    def get(self, request, choice, yes_or_no, ingred, brand):
        last_instance = Kopek_Mama.objects.last()
        category = 'Köpek Mamaları'
        subcategories = [['Kuru Mamalar', '/kopek-mama/1/1/'],
                         ['Yaş Mamalar', '/kopek-mama/1/0/'],
                         ['Yavru Köpek Mamaları', '/kopek-mama/2/1/'],
                         ['Yetişkin Köpek Mamaları', '/kopek-mama/2/0/'],
                         ['Kısır Köpek Mamaları', '/kopek-mama/3/1/']]
        shopby = Kopek_Mama.get_distinct_ingred()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Mama.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Lezzet'
        filtrele = 'yes'
        products = Kopek_Mama.objects.all()
        if brand == 'all':
            if ingred == 'all':
                if choice == 1:
                    products = Kopek_Mama.objects.filter(kuru_or_yas=yes_or_no)
                elif choice == 2:
                    products = Kopek_Mama.objects.filter(yavru_or_yetiskin=yes_or_no)
                elif choice == 3:
                    products = Kopek_Mama.objects.filter(kisir_or_not=yes_or_no)
            else:
                if choice == 1:
                    products = Kopek_Mama.objects.filter(kuru_or_yas=yes_or_no, neyli=ingred)
                elif choice == 2:
                    products = Kopek_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred)
                elif choice == 3:
                    products = Kopek_Mama.objects.filter(kisir_or_not=yes_or_no, neyli=ingred)
                else:
                    products = Kopek_Mama.objects.filter(neyli=ingred)
        else:
            if ingred == 'all':
                if choice == 1:
                    products = Kopek_Mama.objects.filter(kuru_or_yas=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kopek_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, brand=brand)
                elif choice == 3:
                    products = Kopek_Mama.objects.filter(kisir_or_not=yes_or_no, brand=brand)
                else:
                    products = Kopek_Mama.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kopek_Mama.objects.filter(kuru_or_yas=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 2:
                    products = Kopek_Mama.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 3:
                    products = Kopek_Mama.objects.filter(kisir_or_not=yes_or_no, neyli=ingred, brand=brand)
                else:
                    products = Kopek_Mama.objects.filter(neyli=ingred, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Tasma(View):
    def post(self, request, choice, yes_or_no, beden, brand):
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

    def get(self, request, choice, yes_or_no, beden, brand):
        last_instance = Kopek_Tasma.objects.last()
        category = 'Köpek Tasmaları'
        subcategories = [['Göğüs Tasmaları', '/kopek-tasma/1/1/'],
                         ['Boyun Tasmaları', '/kopek-tasma/1/0/'],
                         ['Kumaş Tasmalar', '/kopek-tasma/2/2/'],
                         ['Deri Tasmalar', '/kopek-tasma/2/1/'],
                         ['Zincir Tasmalar', '/kopek-tasma/2/0/']]
        shopby = Kopek_Tasma.get_distinct_ingred()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Tasma.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Beden'
        filtrele = 'yes'
        products = Kopek_Tasma.objects.all()
        if brand == 'all':
            if beden == 'all':
                if choice == 1:
                    products = Kopek_Tasma.objects.filter(gogus_or_boyun=yes_or_no)
                elif choice == 2:
                    products = Kopek_Tasma.objects.filter(deri_or_zincir=yes_or_no)
            else:
                if choice == 1:
                    products = Kopek_Tasma.objects.filter(gogus_or_boyun=yes_or_no, neyli=beden)
                elif choice == 2:
                    products = Kopek_Tasma.objects.filter(deri_or_zincir=yes_or_no, neyli=beden)
                else:
                    products = Kopek_Tasma.objects.filter(neyli=beden)
        else:
            if beden == 'all':
                if choice == 1:
                    products = Kopek_Tasma.objects.filter(gogus_or_boyun=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kopek_Tasma.objects.filter(deri_or_zincir=yes_or_no, brand=brand)
                else:
                    products = Kopek_Tasma.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kopek_Tasma.objects.filter(gogus_or_boyun=yes_or_no, neyli=beden, brand=brand)
                elif choice == 2:
                    products = Kopek_Tasma.objects.filter(deri_or_zincir=yes_or_no, neyli=beden, brand=brand)
                else:
                    products = Kopek_Tasma.objects.filter(neyli=beden, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Odul(View):
    def post(self, request, choice, yes_or_no, ingred, brand):
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

    def get(self, request, choice, yes_or_no, ingred, brand):
        last_instance = Kopek_Odul.objects.last()
        category = 'Köpek Ödülleri'
        subcategories = [['Köpek Kemikleri', '/kopek-odul/1/2/'],
                         ['Köpek Stick Ödülleri', '/kopek-odul/1/1/'],
                         ['Bisküvi Ödüller', '/kopek-odul/1/0/'],
                         ['Yavru Köpek Ödülleri', '/kopek-odul/2/1/'],
                         ['Yetişkin Köpek Ödülleri', '/kopek-odul/2/0/']]
        shopby = Kopek_Odul.get_distinct_ingred()
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Odul.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = 'Lezzet'
        filtrele = 'yes'
        products = Kopek_Odul.objects.all()
        if brand == 'all':
            if ingred == 'all':
                if choice == 1:
                    products = Kopek_Odul.objects.filter(kemik_or_stick_or_biskuvi=yes_or_no)
                elif choice == 2:
                    products = Kopek_Odul.objects.filter(yavru_or_yetiskin=yes_or_no)
            else:
                if choice == 1:
                    products = Kopek_Odul.objects.filter(kemik_or_stick_or_biskuvi=yes_or_no, neyli=ingred)
                elif choice == 2:
                    products = Kopek_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred)
                else:
                    products = Kopek_Odul.objects.filter(neyli=ingred)
        else:
            if ingred == 'all':
                if choice == 1:
                    products = Kopek_Odul.objects.filter(kemik_or_stick_or_biskuvi=yes_or_no, brand=brand)
                elif choice == 2:
                    products = Kopek_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, brand=brand)
                else:
                    products = Kopek_Odul.objects.filter(brand=brand)
            else:
                if choice == 1:
                    products = Kopek_Odul.objects.filter(kemik_or_stick_or_biskuvi=yes_or_no, neyli=ingred, brand=brand)
                elif choice == 2:
                    products = Kopek_Odul.objects.filter(yavru_or_yetiskin=yes_or_no, neyli=ingred, brand=brand)
                else:
                    products = Kopek_Odul.objects.filter(neyli=ingred, brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Oyuncak(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kopek_Oyuncak.objects.last()
        category = 'Köpek Oyuncakları'
        subcategories = [['Diş İpi Oyuncakları', '/kopek-oyuncak/1/2/'],
                         ['Çiğneme Oyuncakları', '/kopek-oyuncak/1/1/'],
                         ['Peluş Oyuncaklar', '/kopek-oyuncak/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Oyuncak.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kopek_Oyuncak.objects.all()
        if brand == 'all':
            if choice == 1:
                products = Kopek_Oyuncak.objects.filter(tur=yes_or_no)
        else:
            if choice == 1:
                products = Kopek_Oyuncak.objects.filter(tur=yes_or_no, brand=brand)
            else:
                products = Kopek_Oyuncak.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Yatak(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kopek_Yatak.objects.last()
        category = 'Köpek Yatakları'
        subcategories = [['Small Yataklar', '/kopek-yatak/1/3/'],
                         ['Medium Yataklar', '/kopek-yatak/1/2/'],
                         ['Large Yataklar', '/kopek-yatak/1/1/'],
                         ['X-Large Yataklar', '/kopek-yatak/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Yatak.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kopek_Yatak.objects.all()
        if brand == 'brand':
            if choice == 1:
                products = Kopek_Yatak.objects.filter(beden=yes_or_no)
        else:
            if choice == 1:
                products = Kopek_Yatak.objects.filter(beden=yes_or_no, brand=brand)
            else:
                products = Kopek_Yatak.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class ProductList_Kopek_Kap(View):
    def post(self, request, choice, yes_or_no, brand):
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

    def get(self, request, choice, yes_or_no, brand):
        last_instance = Kopek_Kap.objects.last()
        category = 'Köpek Mama Kapları'
        subcategories = [['Seramik Kaplar', '/kopek-kap/1/2/'],
                         ['Metal Kaplar', '/kopek-kap/1/1/'],
                         ['Plastik Kaplar', '/kopek-kap/1/0/']]
        shopby = {}
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_brand = basepath_raw[0:last + 1]
        last_2 = int(basepath_brand[:-1].rfind('/'))
        basepath = basepath_brand[0:last_2 + 1]
        shopby2 = Kopek_Kap.get_distinct_brands()
        tail2 = basepath_raw[last + 1:] + '/'
        tail = basepath_brand[last_2 + 1:]
        tail_name = ''
        filtrele = 'no'
        products = Kopek_Kap.objects.all()
        if brand == 'all':
            if choice == 1:
                products = Kopek_Kap.objects.filter(tur=yes_or_no)
        else:
            if choice == 1:
                products = Kopek_Kap.objects.filter(tur=yes_or_no, brand=brand)
            else:
                products = Kopek_Kap.objects.filter(brand=brand)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'last_instance': last_instance,
                                                   'category': category, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'shopby': shopby,
                                                   'filtrele': filtrele,
                                                   'basepath': basepath, 'tail': tail, 'tailname': tail_name,
                                                   'basepathbrand': basepath_brand, 'shopby2': shopby2, 'tail2': tail2,
                                                   'sortby': sortby})


class product_detail(View):
    def post(self, request, slug):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        number = request.POST.get('quantity')
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
                    if number:
                        cart[product] = quantity + int(number)
                    else:
                        cart[product] = quantity + 1
            else:
                if number:
                    cart[product] = int(number)
                else:
                    cart[product] = 1
        else:
            cart = {}
            if number:
                cart[product] = int(number)
            else:
                cart[product] = 1
        request.session['cart'] = cart
        return HttpResponseRedirect(request.path_info)

    def get(self, request, slug):
        product = Products.objects.get(slug=slug)
        you_might_like = []
        for item in Products.get_last_five_products(product.main_category.id):
            if item != product:
                you_might_like.append(item)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        return render(request, 'product.html', {'product': product, 'cart_products': cart_products,
                                                'might_like': you_might_like})


class Search_Products(View):
    def post(self, request, name):
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
        query = request.POST.get('query')
        basepath_raw = request.POST.get('basepathraw')
        return redirect(f'/search/{basepath_raw[8:-1]}/?query={query}')

    def get(self, request, name):
        query = request.GET.get('query')
        raw_query = str(query).replace(' ', '+')
        basepath_raw = self.request.get_full_path()[:-1]
        last = int(basepath_raw.rfind('/'))
        basepath_raw = basepath_raw[0:last + 1]
        products = Products.objects.filter(name__icontains=query)
        subcategories = []
        for product in products:
            if product.brand not in subcategories:
                subcategories.append(product.brand)
        if name != 'all':
            products = Products.objects.filter(name__icontains=query, brand=name)
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        if 'null' in list(cart.keys()):
            del cart['null']
        ids = list(request.session.get('cart').keys())
        cart_products = Products.get_products_by_id(ids)
        #####
        sortby = request.GET.get('sortby')
        if sortby == 'h2l':
            products = products.order_by('-price')
        elif sortby == 'l2h':
            products = products.order_by('price')
        elif products == 'newer':
            products = products.order_by('-updated-at')
        return render(request, 'collection.html', {'products': products, 'cart_products': cart_products,
                                                   'subcategories': subcategories, 'filtrele': 'no', 'basepath': 'none',
                                                   'shopby2': '', 'category': 'Markalar', 'query': query,
                                                   'basepathraw': basepath_raw, 'rawquery': raw_query,
                                                   'sortby': sortby})


class SortBy(View):
    def post(self, request):
        url = request.POST.get('url')
        sortby = request.POST.get('SortBy')
        return redirect(f'{url}?sortby={sortby}')
