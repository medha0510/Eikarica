# Generated by Django 3.0.14 on 2021-07-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0011_auto_20210717_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
    ]
