# Generated by Django 2.0.6 on 2018-07-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infsoc', '0008_auto_20180708_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('LISTO', 'LISTO')], default='PENDIENTE', max_length=255),
        ),
    ]