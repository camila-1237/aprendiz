from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz
from .forms import AprendizForm

def listar_aprendices(request):
    aprendices = Aprendiz.objects.all()
    return render(request, 'aprendices/listar_aprendices.html', {'aprendices': aprendices})

def crear_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_aprendices')
    else:
        form = AprendizForm()
    return render(request, 'aprendices/formulario_aprendiz.html', {'form': form})

