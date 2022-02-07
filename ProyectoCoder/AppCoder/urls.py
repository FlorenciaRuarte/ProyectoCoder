from django.contrib import admin
from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('curso/list', CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', CursoDelete.as_view(), name='Delete'),
]






       