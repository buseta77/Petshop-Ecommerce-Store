# Generated by Django 4.0.3 on 2022-04-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0014_alter_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
