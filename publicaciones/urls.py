
from django.urls import path
from .import views

urlpatterns = [
   
        path('ver-publicaciones/' ,views.Publicacionesview.as_view(), name='publicaciones')
    
    ]
