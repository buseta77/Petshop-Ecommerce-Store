from django.db import models
from .products import Products
from .customer import Customer
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Order(models.Model):
    order_no = models.IntegerField(default=10000, blank=False, unique=True,
                                   validators=[MaxValueValidator(1000000), MinValueValidator(10000)])
    city = models.CharField(max_length=50, default='', blank=False)
    district = models.CharField(max_length=50, default='', blank=False)
    neighborhood = models.CharField(max_length=100, default='', blank=False)
    address = models.CharField(max_length=500, default='', blank=False)
    date = models.DateTimeField(default=datetime.datetime.now)
    charge = models.FloatField(default=0, blank=False)
    cargo = models.FloatField(default=0, blank=False)
    note = models.TextField(max_length=3000, default='', blank=True)
    DURUM_CHOICES = (('Hazırlanıyor', 'Hazırlanıyor'), ('Kargoda', 'Kargoda'), ('Tamamlandı', 'Tamamlandı'))
    durum = models.CharField(max_length=20, choices=DURUM_CHOICES, default='Hazırlanıyor')


class OrderCustomer(Order):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return OrderCustomer.objects.filter(customer=customer_id).order_by('-date')


class OrderGuest(Order):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, default='', blank=False)
    email = models.EmailField(blank=False)

    def placeOrder(self):
        self.save()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    solo_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def register(self):
        self.save()

    @staticmethod
    def get_items_by_order(id):
        return OrderProduct.objects.filter(order=id)