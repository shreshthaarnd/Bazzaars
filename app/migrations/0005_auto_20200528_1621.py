# Generated by Django 2.1.9 on 2020-05-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200528_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storesocialmedia',
            name='id',
        ),
        migrations.AddField(
            model_name='storesocialmedia',
            name='Store_ID',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]