# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import EmpleadoViewSet, ClienteViewSet, MaquinaViewSet, ProductoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'maquinas', MaquinaViewSet)
router.register(r'productos', ProductoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
