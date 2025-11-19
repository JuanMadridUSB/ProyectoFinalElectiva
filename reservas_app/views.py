from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Servicio, Cita
from .forms import ClienteForm, ServicioForm, CitaForm

# Home
def home(request):
    return render(request, 'home.html')


# CLIENTES
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})


# SERVICIOS
def servicio_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio_list.html', {'servicios': servicios})

def servicio_create(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servicio_list')
    return render(request, 'servicio_form.html', {'form': form})

def servicio_update(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    form = ServicioForm(request.POST or None, instance=servicio)
    if form.is_valid():
        form.save()
        return redirect('servicio_list')
    return render(request, 'servicio_form.html', {'form': form})

def servicio_delete(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicio_list')
    return render(request, 'servicio_confirm_delete.html', {'servicio': servicio})


# CITAS
def cita_list(request):
    citas = Cita.objects.all()
    return render(request, 'cita_list.html', {'citas': citas})

def cita_create(request):
    form = CitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cita_list')
    return render(request, 'cita_form.html', {'form': form})

def cita_update(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    form = CitaForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect('cita_list')
    return render(request, 'cita_form.html', {'form': form})

def cita_delete(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('cita_list')
    return render(request, 'cita_confirm_delete.html', {'cita': cita})
