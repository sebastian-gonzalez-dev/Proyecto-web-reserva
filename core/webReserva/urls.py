from django.urls import path
from .views import home_vista, perfil_vista, reservas_vista

urlpatterns = [
    path('', home_vista, name="home"),
    path('perfil/', perfil_vista, name="perfil"),
    path('reservas/', reservas_vista, name="reservas"),
]