# Generated by Django 2.0.6 on 2018-07-08 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infsoc', '0013_auto_20180708_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='comprador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comprador', to='infsoc.Usuario'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendedor', to='infsoc.Usuario'),
        ),
    ]
