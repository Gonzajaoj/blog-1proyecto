from django.shortcuts import render, redirect
from .models import Publicacion
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PublicarForm


# listar las publicaciones
"""def publicaciones_views(request):
    ctx={
        'publicaciones': Publicacion.objects.all()
        
    }
    return render(request, 'publicaciones.html',ctx)
"""
#views basado en clase, para enlistar las publicaciones

class Publicacionesview(ListView):
    template_name='publicaciones/publicaciones.html'
    model= Publicacion
    context_object_name= 'publicaciones'
   
    
def publicar_view(request):
    if request.method == 'POST':
        form = PublicarForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save()
            return redirect('publicaciones')
    else:
        form = PublicarForm()
        ctx = {'form' : form}
        return render(request, 'publicaciones/publicar.html', ctx)

#viwes basada en clase para crear una publicacion
"""class Publicar(CreateView):
    model=Publicacion
    template_name='publicaciones/publicar.html'
    form_clase=PublicarForm"""
 
#views basada en clase para modificar una publicacion
class ModificarPublicacionView(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/modificar-publicacion.html'
    form_class = PublicarForm
    success_url = '../ver-publicaciones/'

 