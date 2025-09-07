from rest_framework import serializers
from .models import student, Asignatura

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ['id', 'nombre']

class EstudianteSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True)

    class Meta:
        model = student
        fields = ['id', 'nombre', 'email', 'asignaturas']

    def create(self, validated_data):
        asignaturas_data = validated_data.pop('asignaturas')
        estudiante = student.objects.create(**validated_data)
        for asignatura_data in asignaturas_data:
            asignatura, created = Asignatura.objects.get_or_create(**asignatura_data)
            estudiante.asignaturas.add(asignatura)
        return estudiante

    def update(self, instance, validated_data):
        asignaturas_data = validated_data.pop('asignaturas')
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Limpiar asignaturas actuales y agregar las nuevas
        instance.asignaturas.clear()
        for asignatura_data in asignaturas_data:
            asignatura, created = Asignatura.objects.get_or_create(**asignatura_data)
            instance.asignaturas.add(asignatura)
        return instance
