# Generated by Django 2.1.9 on 2020-06-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_storeactivationdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storeactivationdata',
            name='MERCHANT_KEY',
        ),
        migrations.RemoveField(
            model_name='storeactivationdata',
            name='MID',
        ),
    ]
