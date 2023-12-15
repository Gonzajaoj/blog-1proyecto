from django.shortcuts import render

# Create your views here.
def publicaciones_views(request):
    return render(request, 'publicaciones.html',{})