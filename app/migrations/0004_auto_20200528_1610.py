# Generated by Django 2.1.9 on 2020-05-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_storelogodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreSocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_Facebook', models.CharField(default='NA', max_length=500)),
                ('Store_Twitter', models.CharField(default='NA', max_length=500)),
                ('Store_Instagram', models.CharField(default='NA', max_length=500)),
            ],
            options={
                'db_table': 'StoreSocialMedia',
            },
        ),
        migrations.RemoveField(
            model_name='storeotherdata',
            name='Store_Facebook',
        ),
        migrations.RemoveField(
            model_name='storeotherdata',
            name='Store_Instagram',
        ),
        migrations.RemoveField(
            model_name='storeotherdata',
            name='Store_Twitter',
        ),
    ]
