from django.shortcuts import render
from django .http import HttpResponse

def hola(request):
    return render(request, 'hola/index.html')
def unidad1(request):
   return HttpResponse(request, 'hola/index.html')
