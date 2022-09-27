from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name='hola'),
    #path('<str:nombre>/', views.saludo, name= 'saludo'),
   # path('Unidad1', views.Unidad1, name= 'Unidad1')
]