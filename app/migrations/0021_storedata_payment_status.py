# Generated by Django 2.1.9 on 2020-06-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_storemerchantdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedata',
            name='Payment_Status',
            field=models.CharField(default='Unpaid', max_length=100),
        ),
    ]