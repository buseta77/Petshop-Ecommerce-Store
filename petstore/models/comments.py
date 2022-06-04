from django.db import models
from .customer import Customer
from .products import Products


class Comment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000, default='', blank=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    RATING_CHOICES = [(i, i) for i in range(1, 6)]
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    commented_at = models.DateTimeField(auto_now_add=True)