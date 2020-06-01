# Generated by Django 2.1.9 on 2020-05-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_storeproductcategorydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreProductData',
            fields=[
                ('Store_ID', models.CharField(max_length=100)),
                ('Product_Category_ID', models.CharField(max_length=100)),
                ('Product_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=500)),
                ('Product_Description', models.CharField(default='Description Not Availiable', max_length=1000)),
                ('Product_Price', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'StoreProductData',
            },
        ),
        migrations.CreateModel(
            name='StoreProductImageData',
            fields=[
                ('Store_ID', models.CharField(max_length=100)),
                ('Product_Category_ID', models.CharField(max_length=100)),
                ('Product_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Product_Image', models.FileField(upload_to='productcategory/')),
            ],
            options={
                'db_table': 'StoreProductImageData',
            },
        ),
        migrations.AlterField(
            model_name='storeproductcategorydata',
            name='Product_Category_ID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='storeproductcategorydata',
            name='Store_ID',
            field=models.CharField(max_length=100),
        ),
    ]