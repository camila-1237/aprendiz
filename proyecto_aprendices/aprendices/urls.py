from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_aprendices, name='listar_aprendices'),
    path('crear/', views.crear_aprendiz, name='crear_aprendiz'),
]
