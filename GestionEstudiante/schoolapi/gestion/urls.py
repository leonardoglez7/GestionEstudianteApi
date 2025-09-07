from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, AsignaturaViewSet, recibir_datos

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'asignaturas', AsignaturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("recibir/", recibir_datos)
]
