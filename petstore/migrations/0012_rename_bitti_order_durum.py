# Generated by Django 4.0.3 on 2022-03-30 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0011_alter_order_bitti'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='bitti',
            new_name='durum',
        ),
    ]