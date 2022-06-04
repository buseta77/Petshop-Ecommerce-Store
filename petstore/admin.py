from django.contrib import admin
from django.contrib.admin import display

from .models import customer, products, orders, main_category, campaigns, subscriptions, comments

class Kedi_MamaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class OrderGuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'durum', 'order_no', 'date']
    list_filter = ['durum', 'date']

class OrderCustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'durum', 'order_no', 'date']
    list_filter = ['durum', 'date']

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'solo_price', 'quantity', 'order_no']
    list_filter = ['order__order_no']

    @display(ordering='order__order_no', description='Sipariş No')
    def order_no(self, obj):
        return obj.order.order_no

class SubsciptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']

# Register your models here.
admin.site.register(main_category.Main_category)
admin.site.register(customer.Customer)
admin.site.register(products.Kedi_Mama, Kedi_MamaAdmin)
admin.site.register(products.Kedi_Kum)
admin.site.register(products.Kedi_Odul)
admin.site.register(products.Kedi_Oyuncak)
admin.site.register(products.Kedi_Tirmalama)
admin.site.register(products.Kedi_Kap)
admin.site.register(products.Kopek_Mama)
admin.site.register(products.Kopek_Kap)
admin.site.register(products.Kopek_Yatak)
admin.site.register(products.Kopek_Tasma)
admin.site.register(products.Kopek_Oyuncak)
admin.site.register(products.Kopek_Odul)
admin.site.register(orders.OrderGuest, OrderGuestAdmin)
admin.site.register(orders.OrderCustomer, OrderCustomerAdmin)
admin.site.register(campaigns.Campaign)
admin.site.register(orders.OrderProduct, OrderProductAdmin)
admin.site.register(subscriptions.Subscription, SubsciptionAdmin)
admin.site.register(comments.Comment)
