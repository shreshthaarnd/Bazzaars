# Generated by Django 2.1.9 on 2020-06-04 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200604_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdata',
            old_name='Cart_Price',
            new_name='Cart_Total',
        ),
    ]
