# Generated by Django 2.1.9 on 2020-05-31 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200529_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedata',
            name='Verify_Status',
            field=models.CharField(default='Unverified', max_length=100),
        ),
    ]
