# Generated by Django 2.1.9 on 2020-05-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreOtherData',
            fields=[
                ('Store_ID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Store_About', models.CharField(default='NA', max_length=1500)),
                ('Store_Facebook', models.CharField(default='NA', max_length=500)),
                ('Store_Twitter', models.CharField(default='NA', max_length=500)),
                ('Store_Instagram', models.CharField(default='NA', max_length=500)),
            ],
            options={
                'db_table': 'StoreOtherData',
            },
        ),
        migrations.AlterField(
            model_name='storedata',
            name='Status',
            field=models.CharField(default='Deactive', max_length=100),
        ),
    ]
