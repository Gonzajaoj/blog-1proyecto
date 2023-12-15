from django.shortcuts import render
#vista basada en una funcion

def index_views(request):
    return render(request, 'index.html', {})


