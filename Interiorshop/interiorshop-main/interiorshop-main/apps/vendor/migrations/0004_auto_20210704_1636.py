# Generated by Django 3.0.14 on 2021-07-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cart',
            field=models.IntegerField(),
        ),
    ]