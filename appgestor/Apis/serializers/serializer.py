import base64
from rest_framework import serializers
from appgestor.models import *
from drf_extra_fields.fields import Base64ImageField

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RolVistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RolVista
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class VistaSerializer(serializers.ModelSerializer):
    nombre_modulo = serializers.CharField(source="modulo_id.nombre", read_only=True)
    class Meta:
        model= Vista
        fields= [
            "id",
            "nombre",
            "descripcion",
            "icono",
            "ruta",
            "modulo_id",
            "nombre_modulo",
        ]
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class UsuarioSerializer(serializers.ModelSerializer):
    tipoDocumento_nombre = serializers.CharField(source="tipoDocumento.nombre", read_only=True)
    class Meta:
        model= Usuario
        fields = [
            "id",
            "correo",
            "nombres",
            "contrasena",
            "apellidos",
            "documento",
            "tipoDocumento",
            "tipoDocumento_nombre"
        ]
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }
        
class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoDocumento
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }


class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioRol
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RecuperarContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RecuperarContrasena
        fields= '__all__'

class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)
    
class EnviarCodigoSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    
class VerificarCodigoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)
    usuario_id = serializers.IntegerField()

#p

class InstructorSerializer(serializers.ModelSerializer):
    foto = serializers.CharField(required=False, allow_null=True)  # Recibimos Base64 como string
    nombre_tipo_vinculacion = serializers.CharField(source="tipo_vinculacion_id.nombre", read_only=True)

    class Meta:
        model = Instructor
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True},
            'horas_asignadas': {'default': 0}
        }

    def create(self, validated_data):
        # Convertir Base64 a binario si se proporciona una imagen
        foto_base64 = validated_data.pop('foto', None)
        if foto_base64:
            try:
                validated_data['foto'] = base64.b64decode(foto_base64)
            except Exception as e:
                raise serializers.ValidationError({"foto": "Error al decodificar la imagen Base64."})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Manejar actualización de la foto
        foto_base64 = validated_data.pop('foto', None)
        if foto_base64:
            try:
                instance.foto = base64.b64decode(foto_base64)
            except Exception as e:
                raise serializers.ValidationError({"foto": "Error al decodificar la imagen Base64."})
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        """Convierte la imagen binaria a Base64 cuando se consulta."""
        data = super().to_representation(instance)
        if instance.foto:
            data["foto"] = base64.b64encode(instance.foto).decode("utf-8")  # Convierte a Base64
        return data
        
class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True},
            'capacidad': {'default': 0}  # Cambio aquí
        }
        
class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True},
            'ano': {'default': 0}  # Cambio aquí
        }

class NivelFormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelFormacion
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class TipoVinculacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVinculacion
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class ResultadoAprendizajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoAprendizaje
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }


class FaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fase
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }


class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ficha
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }
        


class ConsolidadoAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsolidadoAmbiente
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
            
        
        }

class InstructorHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorHorario
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }
