# Generated by Django 4.0.3 on 2022-03-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0002_rename_litre_kedi_kum_neyli'),
    ]

    operations = [
        migrations.AddField(
            model_name='kedi_tirmalama',
            name='karton_or_ahsap',
            field=models.CharField(choices=[('1', 'karton'), ('0', 'ahsap')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
