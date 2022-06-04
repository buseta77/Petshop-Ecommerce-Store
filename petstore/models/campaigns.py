from django.db import models
from .products import Products
from .customer import Customer


class Campaign(models.Model):
    title = models.CharField(max_length=50, default='')
    header = models.CharField(max_length=70, default='')
    image_885x450 = models.ImageField(upload_to='uploads/campaigns/')
    image_880x285 = models.ImageField(upload_to='uploads/campaigns/')
    image_square = models.ImageField(upload_to='uploads/campaigns/')
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(max_length=5000, default='', blank=True, null=True, help_text='HTML')
    TYPE_CHOICES = (('genel', 'genel', ), ('kedi', 'kedi'), ('köpek', 'köpek'))
    campaign_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_campaigns():
        return Campaign.objects.all().order_by('-updated_at')

    @staticmethod
    def get_campaigns_by_type(campaign_type):
        return Campaign.objects.filter(campaign_type=campaign_type).order_by('-updated_at')
