from django.db import models


class Main_category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_main_categories():
        return Main_category.objects.all()

    def __str__(self):
        return self.name
