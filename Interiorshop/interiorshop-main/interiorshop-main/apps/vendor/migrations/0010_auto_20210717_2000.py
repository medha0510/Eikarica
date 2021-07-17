# Generated by Django 3.0.14 on 2021-07-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0009_remove_vendor_rpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='aadhaar_card',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact_no',
            field=models.IntegerField(default='null', unique=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='pan_card',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
