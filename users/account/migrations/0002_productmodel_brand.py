# Generated by Django 3.2.10 on 2021-12-09 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
