# Generated by Django 2.0.6 on 2018-07-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infsoc', '0002_auto_20180707_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linea',
            name='numero',
            field=models.IntegerField(),
        ),
    ]