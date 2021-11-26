from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Paciente, Tessiu 
 
class PacienteAdmin(admin.ModelAdmin):
     list_display = ('name',)
 
admin.site.register(Paciente, PacienteAdmin)
 
 
class TessiuAdmin(admin.ModelAdmin):
    list_display = ('color','temperatura','inflamation','name')
    list_filter=('color','name',)
    #readonly_fields=('color',)
    ordering = ('color',)
    search_fields = ('color',)

admin.site.register(Tessiu,TessiuAdmin)
