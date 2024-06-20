from django.urls import path
from app1 import views 

urlpatterns = [
    path('',views.index, name='inicio'),
    path('mas_info/',views.mas_info, name='informacion'),
    path('terminos_uso/',views.terminos_uso, name='terminos'),
    path('politica_privacidad/',views.politica_privacidad, name='politica'),
    path('soporte/',views.soporte_tecnico, name='soporte'),
    path('obreros/',views.obreros_vista, name='obreros'),
    path('epps/',views.epps, name='epps'),
    path('or/',views.ordenes_retiro, name='or'),
]