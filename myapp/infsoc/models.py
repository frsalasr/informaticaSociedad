from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

class Medicamento(models.Model):
	nombre = models.CharField(max_length=255)
	miligramos = models.IntegerField()

	def __str__(self):
		return self.nombre + ' ' + str(self.miligramos) + ' mg'


class Comuna(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

class Linea(models.Model):
	numero = models.IntegerField(unique=False, blank=True)
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['numero']

class Metro(models.Model):
	numero = models.IntegerField(default=1)
	nombre = models.CharField(max_length=255)
	linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
	comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ['numero']

class Transaccion(models.Model):
	ESTADO = (
	    ('PUESTO', 'PUESTO'),
	    ('CONTACTADO','CONTACTADO'),
	    ('LISTO', 'LISTO'),
	)

	TIPO = (
		('VENTA', 'VENTA'),
		('COMPRA', 'COMPRA'),
		('REGALO', 'REGALO'),
	)

	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=False, blank=False)
	vendedor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='vendedor')
	comprador = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comprador')
	tipo = models.CharField(max_length=255, choices=TIPO)
	estado = models.CharField(max_length=255, choices=ESTADO, default='PUESTO')
	precio = models.IntegerField(default=0)
	comunas = models.ManyToManyField(Comuna, null=True, blank=True)
	lineas = models.ManyToManyField(Linea)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		if self.vendedor is None:
			return self.comprador.first_name + ' ' + self.tipo + ' ' + str(self.medicamento) + ' ' + self.estado
		else:
			return self.vendedor.first_name + ' ' + self.tipo + ' ' + str(self.medicamento) + ' ' + self.estado