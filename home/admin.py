from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Paciente, Tessiu 

# Register your models here.
# @admin.register()

# class Admin(admin.ModelAdmin):
#     '''Admin View for '''

#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)
#     date_hierarchy = ''
#     ordering = ('',)
 
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

