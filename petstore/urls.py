from django.urls import path
from .views.home import Index, AboutUs, ContactUs, Subscribe, increase, decrease, addToCart
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView, myOrder, orderSorgula
from .views.campaign import Campaign, CampaignAll
from .middlewares.auth import auth_middleware
from .views.product_page import ProductList, product_detail, ProductList_Kedi_Mama, ProductList_Kedi_Kum,\
	ProductList_Kedi_Odul, ProductList_Kedi_Kap, ProductList_Kedi_Oyuncak, ProductList_Kedi_Tirmalama,\
	ProductList_Kopek_Yatak, ProductList_Kopek_Tasma, ProductList_Kopek_Oyuncak, ProductList_Kopek_Odul,\
	ProductList_Kopek_Mama, ProductList_Kopek_Kap, Search_Products, SortBy


urlpatterns = [
path('', Index.as_view(), name='homepage'),
path('signup/', Signup.as_view(), name='signup'),
path('login/', Login.as_view(), name='login'),
path('logout/', logout, name='logout'),
path('cart/', Cart.as_view(), name='cart'),
path('checkout/', CheckOut.as_view(), name='checkout'),
path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
path('products/<str:slug>/', product_detail.as_view(), name='productdetail'),
path('collection/<int:id>/all/<str:brand>/', ProductList.as_view(), name='collection'),
path('kedi-mama/<int:choice>/<int:yes_or_no>/<str:ingred>/<str:brand>/', ProductList_Kedi_Mama.as_view(), name='kedi-mama'),
path('kedi-kum/<int:choice>/<int:yes_or_no>/<str:litre>/<str:brand>/', ProductList_Kedi_Kum.as_view(), name='kedi-kum'),
path('kedi-odul/<int:choice>/<int:yes_or_no>/<str:ingred>/<str:brand>/', ProductList_Kedi_Odul.as_view(), name='kedi-odul'),
path('kedi-oyuncak/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kedi_Oyuncak.as_view(), name='kedi-oyuncak'),
path('kedi-tirmalama/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kedi_Tirmalama.as_view(), name='kedi-tirmalama'),
path('kedi-kap/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kedi_Kap.as_view(), name='kedi-kap'),
path('kopek-mama/<int:choice>/<int:yes_or_no>/<str:ingred>/<str:brand>/', ProductList_Kopek_Mama.as_view(), name='kopek-mama'),
path('kopek-tasma/<int:choice>/<int:yes_or_no>/<str:beden>/<str:brand>/', ProductList_Kopek_Tasma.as_view(), name='kopek-tasma'),
path('kopek-odul/<int:choice>/<int:yes_or_no>/<str:ingred>/<str:brand>/', ProductList_Kopek_Odul.as_view(), name='kopek-odul'),
path('kopek-oyuncak/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kopek_Oyuncak.as_view(), name='kopek-oyuncak'),
path('kopek-yatak/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kopek_Yatak.as_view(), name='kopek-yatak'),
path('kopek-kap/<int:choice>/<int:yes_or_no>/all/<str:brand>/', ProductList_Kopek_Kap.as_view(), name='kopek-kap'),
path('about-us/', AboutUs.as_view(), name='about-us'),
path('contact-us/', ContactUs.as_view(), name='contact-us'),
path('search/<str:name>/', Search_Products.as_view(), name='search'),
path('sort-by/', SortBy.as_view(), name='sortby'),
path('subscribe/', Subscribe.as_view(), name='subscribe'),
path('decrease/', decrease, name='decrease'),
path('increase/', increase, name='increase'),
path('addToCart/', addToCart, name='addToCart'),
path('campaigns/<str:slug>/', Campaign.as_view(), name='campaign'),
path('campaigns/', CampaignAll.as_view(), name='campaignAll'),
path('my-order/', myOrder.as_view(), name='myOrder'),
path('sorgula/', orderSorgula.as_view(), name='sorgula')
]
