from django.forms import ModelForm
from django import forms
from .models import *

class TransaccionForm(ModelForm):

	class Meta:
		model = Transaccion
		fields = ['tipo', 'precio', 'lineas']
		help_texts = {
			'lineas': 'Mantenga control apretado para elegir más de una línea.',
			'tipo': 'Tipo de transacción: venta, compra o regalo.',
		}

class LoginForm(forms.Form):
	usuario = forms.CharField()
	password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)