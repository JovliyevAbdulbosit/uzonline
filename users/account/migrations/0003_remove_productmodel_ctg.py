# Generated by Django 3.2.10 on 2021-12-09 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_productmodel_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='ctg',
        ),
    ]
