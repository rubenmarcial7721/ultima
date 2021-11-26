from django.urls import path
from .views import sintactico

#app_name = AppName

urlpatterns = [
    path('sintactico/', sintactico, name="sintactico")
]