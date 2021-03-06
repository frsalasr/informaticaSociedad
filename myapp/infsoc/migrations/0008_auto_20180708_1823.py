# Generated by Django 2.0.6 on 2018-07-08 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infsoc', '0007_auto_20180707_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('VENTA', 'VENTA'), ('COMPRA', 'COMPRA'), ('REGALO', 'REGALO')], default='PENDIENTE', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'PENDIENTE'), ('LISTO', 'LISTO')], max_length=255),
        ),
    ]
