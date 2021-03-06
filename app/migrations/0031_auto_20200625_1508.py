# Generated by Django 2.1.9 on 2020-06-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20200623_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproductdata',
            name='Product_Origin',
            field=models.CharField(default='India', max_length=500),
        ),
        migrations.AlterField(
            model_name='cartproductdata',
            name='Product_Add_Date',
            field=models.CharField(default='25/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='feedbackdata',
            name='Feedback_Date',
            field=models.CharField(default='25/06/2020', max_length=15),
        ),
        migrations.AlterField(
            model_name='orderdata',
            name='Order_Date',
            field=models.CharField(default='25/06/2020', max_length=50),
        ),
    ]
