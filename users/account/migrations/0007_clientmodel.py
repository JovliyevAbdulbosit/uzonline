# Generated by Django 3.2.10 on 2021-12-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20211212_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_client', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
            ],
        ),
    ]
