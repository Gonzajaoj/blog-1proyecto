
from django.urls import path
from .import views

urlpatterns = [
   
        path('ver-publicaciones/' ,views.Publicacionesview.as_view(), name='publicaciones'),
        path('publicar/', views.publicar_view, name='publicar'),
        path('modificar/<int:pk>', views.ModificarPublicacionView.as_view(), name= 'modificar-publicacion' )
    
    ]
