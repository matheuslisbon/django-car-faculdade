from django.urls import path
from . import views

urlpatterns = [
    path('carros/adicionar/', views.adicionar_carro, name='adicionar_carro'),
    path('carros/', views.lista_carros, name='lista_carros'),
]