# Generated by Django 3.1.3 on 2020-11-19 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201118_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='additional_information',
        ),
    ]
