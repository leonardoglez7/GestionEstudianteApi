from rest_framework import viewsets
from .models import student, Asignatura
from .serializer import EstudianteSerializer, AsignaturaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = EstudianteSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

@api_view(['POST'])
def recibir_datos(request):
    nombre = request.data.get("nombre")
    email = request.data.get("email")
    asignaturas_data = request.data.get("asignaturas", [])  # lista de dicts

    # Crear el estudiante primero (sin asignaturas)
    estu = student.objects.create(nombre=nombre, email=email)

    # Crear y asociar asignaturas
    for asignatura in asignaturas_data:
        nombre_asignatura = asignatura.get("nombre")
        if nombre_asignatura:
            obj, creado = Asignatura.objects.get_or_create(nombre=nombre_asignatura)
            estu.asignaturas.add(obj)

    return Response({
        "realizado": "hecho",
        "estudiante": estu.nombre
    })
