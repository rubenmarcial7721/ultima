from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tessiu
import pandas as pd
from scipy.spatial import distance
tessiu = Tessiu.objects.all()

# Create your views here.
def home(request):

    #return HttpResponse("Home")
    
    l= Tessiu.objects.get_queryset()
    template_name = "home/index.html" 
    listaProcesada = procesaLista(l)
    distancia= euclidea(l)
    return render(request, template_name, {'lista':l,'listaproc':listaProcesada,'euclidea':distancia})
    
        
def nohome(request):
    print("SALUDOS A LA BANDA")
    
    return HttpResponse("BANDA")

def procesaLista(lista):
    #Hacer algo con la lista
    lista1=[]
    for elemento in lista:
        valor=elemento.temperatura**2 + elemento.inflamation**2 + elemento.color**2
        p=valor**0.5
        if  p > 100:
            lista1.append(p)
    return lista1

def euclidea(tejidos):
    tejidosTotal = []
    for i in tejidos:
        tejido = []
        tejido.append(i.temperatura)
        tejido.append(i.color)
        tejido.append(i.inflamation)
        tejidosTotal.append(tejido)      

    mEuclidea = []
    for i in range(len(tejidosTotal)):
        f = []
        for j in range(len(tejidosTotal)):
            f.append(round(distance.euclidean(tejidosTotal[i],tejidosTotal[j], 6 )))
        mEuclidea.append(f)

    return mEuclidea

def procesa(request):
    if(request.method == 'POST'):
        umbral = int(request.POST['umbral'])
        
    return render(request, 'index.html' , {'Tessiu': tessiu, 'euclidea':euclidea(tessiu) , 'umbral':umbral})
   

