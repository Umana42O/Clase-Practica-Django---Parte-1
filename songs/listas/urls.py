from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<str:name>', descripcion, name='descripcion'),
]
