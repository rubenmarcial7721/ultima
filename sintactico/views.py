from django.shortcuts import render

# Create your views here.

def sintactico(request):
    
    template_name = "sintactico/sintactico.html"
    return render(request, template_name, {})
    