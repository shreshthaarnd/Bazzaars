# Generated by Django 2.1.9 on 2020-06-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200625_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedata',
            name='Join_Date',
            field=models.CharField(default=15, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartproductdata',
            name='Product_Add_Date',
            field=models.CharField(default='29/06/2020', max_length=50),
        ),
        migrations.AlterField(
            model_name='feedbackdata',
            name='Feedback_Date',
            field=models.CharField(default='29/06/2020', max_length=15),
        ),
        migrations.AlterField(
            model_name='orderdata',
            name='Order_Date',
            field=models.CharField(default='29/06/2020', max_length=50),
        ),
    ]
