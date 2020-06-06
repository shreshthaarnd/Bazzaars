# Generated by Django 2.1.9 on 2020-06-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200605_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproductdata',
            name='Product_Add_Date',
            field=models.CharField(default='06/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderdata',
            name='Order_Date',
            field=models.CharField(default='06/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='BANKNAME',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='BANKTXNID',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='CHECKSUMHASH',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='CURRENCY',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='GATEWAYNAME',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='MERCHANT_KEY',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='MID',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='Order_ID',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='PAYMENTMODE',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='RESPCODE',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='RESPMSG',
            field=models.CharField(blank=True, default='None', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='STATUS',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='TXNAMOUNT',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='TXNDATE',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderpaymentdata',
            name='TXNID',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
    ]
