from django.db import models
from .main_category import Main_category


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    price_before = models.IntegerField(default=0)
    main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE, default=1)
    brand = models.CharField(max_length=30, default='')
    #short_description = models.TextField(max_length=1000, default='', blank=True, help_text='HTML')
    description = models.TextField(max_length=5000, default='', blank=True, null=True, help_text='HTML')
    image = models.ImageField(upload_to='uploads/products/')
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_product_number():
        return Products.objects.all().count()

    @staticmethod
    def get_all_products_by_main_category(category_id):
        if category_id:
            return Products.objects.filter(main_category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def get_distinct_brands(category_id):
        return Products.objects.filter(main_category=category_id).order_by().values('brand').distinct()

    @staticmethod
    def get_last_five_products(category_id):
        return Products.objects.filter(main_category=category_id).order_by('updated_at')[:5]


class Kedi_Mama(Products):
    KURUYAS_CHOICES = (('1', 'kuru'), ('0', 'yas'))
    YAVRUYETISKIN_CHOICES = (('1', 'yavru'), ('0', 'yetiskin'))
    KISIRNOT_CHOICES = (('1', 'kisir'), ('0', 'not'))
    kuru_or_yas = models.CharField(max_length=1, choices=KURUYAS_CHOICES)
    yavru_or_yetiskin = models.CharField(max_length=1, choices=YAVRUYETISKIN_CHOICES)
    kisir_or_not = models.CharField(max_length=1,  choices=KISIRNOT_CHOICES)
    neyli = models.CharField(max_length=50, default='')

    @staticmethod
    def get_all_products():
        return Kedi_Mama.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Mama.objects.all().count()

    @staticmethod
    def get_distinct_ingred():
        return Kedi_Mama.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Mama.objects.order_by().values('brand').distinct()

    def get_class_name(self):
        return self.__name__


class Kedi_Kum(Products):
    TUR_CHOICES = (('1', 'silika'), ('0', 'bentonit'))
    OZELLIK_CHOICES = (('1', 'topaklanan'), ('0', 'emici'))
    silika_or_bentonit = models.CharField(max_length=1, choices=TUR_CHOICES)
    topaklanan_or_emici = models.CharField(max_length=1, choices=OZELLIK_CHOICES)
    neyli = models.CharField(max_length=10, default='')

    @staticmethod
    def get_all_products():
        return Kedi_Kum.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Kum.objects.all().count()

    @staticmethod
    def get_distinct_neyli():
        return Kedi_Kum.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Kum.objects.order_by().values('brand').distinct()


class Kedi_Odul(Products):
    TUR_CHOICES = (('1', 'biskuvi'), ('0', 'stick'))
    YAVRUYETISKIN_CHOICES = (('1', 'yavru'), ('0', 'yetiskin'))
    biskuvi_or_stick = models.CharField(max_length=1, choices=TUR_CHOICES)
    yavru_or_yetiskin = models.CharField(max_length=1, choices=YAVRUYETISKIN_CHOICES)
    neyli = models.CharField(max_length=50, default='')

    @staticmethod
    def get_all_products():
        return Kedi_Odul.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Odul.objects.all().count()

    @staticmethod
    def get_distinct_neyli():
        return Kedi_Odul.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Odul.objects.order_by().values('brand').distinct()


class Kedi_Oyuncak(Products):
    TUR_CHOICES = (('3', 'tunel'), ('2', 'lazer'), ('1', 'oltali'), ('0', 'pelus'))
    oltali_or_pelus = models.CharField(max_length=1, choices=TUR_CHOICES)

    @staticmethod
    def get_all_products():
        return Kedi_Oyuncak.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Oyuncak.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Oyuncak.objects.order_by().values('brand').distinct()


class Kedi_Tirmalama(Products):
    TUR_CHOICES = (('1', 'karton'), ('0', 'ahsap'))
    karton_or_ahsap = models.CharField(max_length=1, choices=TUR_CHOICES)

    @staticmethod
    def get_all_products():
        return Kedi_Tirmalama.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Tirmalama.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Tirmalama.objects.order_by().values('brand').distinct()


class Kedi_Kap(Products):
    TUR_CHOICES = (('1', 'seramik'), ('0', 'plastik'))
    seramik_or_plastik = models.CharField(max_length=1, choices=TUR_CHOICES)

    @staticmethod
    def get_all_products():
        return Kedi_Kap.objects.all()

    @staticmethod
    def get_product_number():
        return Kedi_Kap.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kedi_Kap.objects.order_by().values('brand').distinct()


class Kopek_Mama(Products):
    KURUYAS_CHOICES = (('1', 'kuru'), ('0', 'yas'))
    YAVRUYETISKIN_CHOICES = (('1', 'yavru'), ('0', 'yetiskin'))
    KISIRNOT_CHOICES = (('1', 'kisir'), ('0', 'not'))
    kuru_or_yas = models.CharField(max_length=1, choices=KURUYAS_CHOICES)
    yavru_or_yetiskin = models.CharField(max_length=1, choices=YAVRUYETISKIN_CHOICES)
    kisir_or_not = models.CharField(max_length=1, choices=KISIRNOT_CHOICES)
    neyli = models.CharField(max_length=50, default='')

    @staticmethod
    def get_all_products():
        return Kopek_Mama.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Mama.objects.all().count()

    @staticmethod
    def get_distinct_neyli():
        return Kopek_Mama.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_ingred():
        return Kopek_Mama.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Mama.objects.order_by().values('brand').distinct()


class Kopek_Tasma(Products):
    TUR_CHOICES = (('1', 'gogus'), ('0', 'boyun'))
    DERIZINCIR_CHOICES = (('2', 'kumas'), ('1', 'deri'), ('0', 'zincir'))
    gogus_or_boyun = models.CharField(max_length=1, choices=TUR_CHOICES)
    deri_or_zincir = models.CharField(max_length=1, choices=DERIZINCIR_CHOICES)
    neyli = models.CharField(max_length=50, default='')

    @staticmethod
    def get_all_products():
        return Kopek_Tasma.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Tasma.objects.all().count()

    @staticmethod
    def get_distinct_ingred():
        return Kopek_Tasma.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Tasma.objects.order_by().values('brand').distinct()


class Kopek_Odul(Products):
    TUR_CHOICES = (('2', 'kemik'), ('1', 'stick'), ('0', 'biskuvi'))
    YAVRUYETISKIN_CHOICES = (('1', 'yavru'), ('0', 'yetiskin'))
    kemik_or_stick_or_biskuvi = models.CharField(max_length=1, choices=TUR_CHOICES)
    yavru_or_yetiskin = models.CharField(max_length=1, choices=YAVRUYETISKIN_CHOICES)
    neyli = models.CharField(max_length=50, default='')

    @staticmethod
    def get_all_products():
        return Kopek_Odul.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Odul.objects.all().count()

    @staticmethod
    def get_distinct_ingred():
        return Kopek_Odul.objects.order_by().values('neyli').distinct()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Odul.objects.order_by().values('brand').distinct()


class Kopek_Oyuncak(Products):
    TUR_CHOICES = (('2', 'dis ipi'), ('1', 'cigneme'), ('0', 'pelus'))
    tur = models.CharField(max_length=1, choices=TUR_CHOICES)

    @staticmethod
    def get_all_products():
        return Kopek_Oyuncak.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Oyuncak.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Oyuncak.objects.order_by().values('brand').distinct()


class Kopek_Yatak(Products):
    BEDEN_CHOICES = (('3', 'small'), ('2', 'medium'), ('1', 'large'), ('0', 'xlarge'))
    beden = models.CharField(max_length=1, choices=BEDEN_CHOICES)

    @staticmethod
    def get_all_products():
        return Kopek_Yatak.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Yatak.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Yatak.objects.order_by().values('brand').distinct()


class Kopek_Kap(Products):
    TUR_CHOICES = (('2', 'seramik'), ('1', 'metal'), ('0', 'plastik'))
    tur = models.CharField(max_length=1, choices=TUR_CHOICES)

    @staticmethod
    def get_all_products():
        return Kopek_Kap.objects.all()

    @staticmethod
    def get_product_number():
        return Kopek_Kap.objects.all().count()

    @staticmethod
    def get_distinct_brands():
        return Kopek_Kap.objects.order_by().values('brand').distinct()

