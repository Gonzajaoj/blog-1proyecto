from django.shortcuts import render
from .models import Publicacion
from django.views.generic import ListView
 


# listar las publicaciones
"""def publicaciones_views(request):
    ctx={
        'publicaciones': Publicacion.objects.all()
        
    }
    return render(request, 'publicaciones.html',ctx)
"""
#views basado en clase, para enlistar las publicaciones

class Publicacionesview(ListView):
    template_name='publicaciones.html'
    model= Publicacion
    context_object_name= 'publicaciones'