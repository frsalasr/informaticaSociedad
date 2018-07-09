from django.shortcuts import render, redirect, get_object_or_404, render_to_response, redirect
from django.db.models import Q

from .forms import *
from .models import *

from django.contrib.auth import login as auth_login, authenticate
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.http import HttpResponse
import json

# Create your views here.
def home(request):
	template = 'infsoc/home.html'

	return render(request, template, {})

def login(request):
	
	template = 'infsoc/login.html'
	
	if request.method == 'POST':
		print (request.POST)
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data.get('usuario')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=user, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				return render(request, template, {'form':form, 
										'error': 'usuario no encontrado'})
	
	form = LoginForm()

	return render(request, template, {'form':form})

def buscador(request):

	template = 'infsoc/buscador.html'
	form = TransaccionForm()

	if request.method == "POST":
		
		medicamento = request.POST.get('search_field').split()[0]
		print(Medicamento)
		if Medicamento.objects.filter(nombre=medicamento).count() > 0:
			med = Medicamento.objects.get(nombre = request.POST.get('search_field').split()[0])
			tipo = request.POST.get('tipo')
			lineas = request.POST.getlist('lineas')

			tr = Transaccion.objects.filter(medicamento=med, tipo=tipo, estado="PUESTO")
			print(tr)
			exclude_list = []
			for trans in tr:
				l = trans.lineas.all()
				for item in l:
					if str(item.id) in lineas:
						#print(item)
						break
				exclude_list.append(item.id)
			if len(exclude_list) > 0:
				tr = Transaccion.objects.filter(medicamento=med, tipo=tipo, estado="PUESTO").exclude(id__in=exclude_list)
				print(tr)

			return render(request, template, {'transacciones': tr})

			#return buscar(request, medicamento)	

		medicamentos = Medicamento.objects.all()
		medicamentos_list = []
		for medicamento in medicamentos:
			medicamentos_list.append(str(medicamento))

		json_medicamento = json.dumps(medicamentos_list)
		#print(json_alimentos)

		return render(request, template, {'medicamentos':json_medicamento ,
								          'error': 'no se encontro el medicamento',
								          'form': form})


	medicamentos = Medicamento.objects.all()
	medicamentos_list = []
	for medicamento in medicamentos:
		medicamentos_list.append(str(medicamento))

	json_medicamento = json.dumps(medicamentos_list)
	#print(json_alimentos)

	return render(request, template, {'medicamentos':json_medicamento, 
									  'form': form})


def buscar(request, id_transaccion):
	print('Llegue!')

	template = 'infsoc/transaccion.html'

	tr = Transaccion.objects.get(id=id_transaccion)

	if request.method == "POST":
		if tr.tipo in ["VENTA", "REGALO"]:
			tr.comprador = request.user
			tr.estado = 'CONTACTADO'
			tr.save()
			return render(request, template, {'aprobado': 'Transacción completada, favor contactarse con ' +str(tr.vendedor.first_name)})

		elif tr.tipo == "COMPRA":
			tr.vendedor = request.user
			tr.estado = 'CONTACTADO'
			tr.save()
			return render(request, template, {'aprobado': 'Transacción completada, favor contactarse con ' +str(tr.comprador.first_name)})

		else:
			return HttpResponse('Error!')



	return render(request, template, {'transaccion': tr})

def crearTransaccion(request):

	template = 'infsoc/crearTransaccion.html'

	if request.method == "POST":
		#print(request.POST.get('search_field').split()[0])
		#print(request.POST)
		medicamento = Medicamento.objects.get(nombre = request.POST.get('search_field').split()[0])
		tipo = request.POST.get('tipo')
		lineas = request.POST.getlist('lineas')
		precio = request.POST.get('precio')
		print(lineas)
		#print(medicamento)

		if tipo == "COMPRA":
			comprador = request.user
			#print(comprador)
			t = Transaccion(medicamento=medicamento,
							comprador=comprador,
							tipo=tipo)
			t.save()
			for linea in lineas:
				t.lineas.add(linea)
			t.save()

			return render(request, template, {'aprobado': 'Transacción para ' + str(medicamento) + ' creada correctamente.'})


		elif tipo == "VENTA":
			vendedor = request.user
			#print(vendedor)
			t = Transaccion(medicamento=medicamento,
							vendedor=vendedor,
							tipo=tipo,
							precio=precio)
			t.save()
			for linea in lineas:
				t.lineas.add(linea)
			t.save()

			return render(request, template, {'aprobado': 'Transacción para ' + str(medicamento) + ' creada correctamente.'})

		elif tipo == "REGALO":
			regalador = request.user
			t = Transaccion(medicamento=medicamento,
							vendedor=regalador,
							tipo=tipo,
							precio=0)
			t.save()
			for linea in lineas:
				t.lineas.add(linea)
			t.save()

			return render(request, template, {'aprobado': 'Transacción para ' + str(medicamento) + ' creada correctamente.'})


		


	"""
	medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=False, blank=False)
	vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name='vendedor')
	comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, related_name='comprador')
	tipo = models.CharField(max_length=255, choices=TIPO)
	estado = models.CharField(max_length=255, choices=ESTADO, default='PENDIENTE')
	precio = models.IntegerField(null=True, blank=True)
	comunas = models.ManyToManyField(Comuna, null=False, blank=False)
	lineas = models.ManyToManyField(Linea)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	"""

	form = TransaccionForm()
	medicamentos = Medicamento.objects.all()
	medicamentos_list = []
	for medicamento in medicamentos:
		medicamentos_list.append(str(medicamento))

	json_medicamento = json.dumps(medicamentos_list)
	#print(json_alimentos)

	return render(request, template, {'medicamentos':json_medicamento,
									  'form': form})


def transacciones(request):

	template = 'infsoc/transacciones.html'

	tr = Transaccion.objects.filter(Q(comprador=request.user) | Q(vendedor=request.user)).order_by('estado')

	return render(request, template, {'transacciones1': tr })