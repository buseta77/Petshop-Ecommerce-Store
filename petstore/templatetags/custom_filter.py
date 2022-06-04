from django import template
from petstore.models.orders import OrderProduct

register = template.Library()


@register.filter(name='currency')
def currency(number):
    return str(number) + ' TL'


@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1

@register.filter(name='items_in_order')
def items_in_order(id):
    return OrderProduct.get_items_by_order(id)