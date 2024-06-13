from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_vista(request):
    return render(request, 'core/index.html')

@login_required
def perfil_vista(request):
    return render(request,'account/perfil.html')


@login_required
def reservas_vista(request):
    return render(request, 'reservas.html')