from rest_framework import routers
from .api import Visualizadordatos1
from django.urls import path
from django.conf.urls import url,include
from . import views
router = routers.DefaultRouter()
router.register('',Visualizadordatos1)
urlpatterns = [
    url(r'DB/',include(router.urls)),
    url(r'ObtieneArchivo/(?P<parametro>[\w\-]+)/$',views.GetDatos),
    url(r'estadisticaDesdeArchivo/',views.EstadisticaDesdeArchivo),
    url(r'mostrarEnMapa/',views.MostrarEnMapa),
    url(r'ObtieneNombres/',views.GetNombres)
]