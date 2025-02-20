from rest_framework import serializers
from appgestor.models import *

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
    vista_rol = serializers.CharField(read_only=True)
    vista_nombre = serializers.CharField(read_only=True)
    class Meta:
        model= RolVista
        fields= [
            "id",
            "rol_id_id",
            "vista_rol",
            "vista_id_id",
            "vista_nombre"
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

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioRol
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
