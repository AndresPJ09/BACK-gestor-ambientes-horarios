from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone  # ✅ Importar timezone correctamente
from yaml import serialize

from appgestor.Business.recuperarContrasena_service import RecuperarContrasenaService
from appgestor.Business.rolVista_service import RolVistaService
from appgestor.Business.usuario_service import UsuarioService
from appgestor.Entity.Dao.rolvista_dao import RolVistaDAO
from appgestor.Entity.Dao.vista_dao import VistaDAO
from appgestor.models import  Ambiente, Competencia, Instructor, Modulo, NivelFormacion, Periodo, Programa, RecuperarContrasena, ResultadoAprendizaje, Rol, \
    RolVista, TipoVinculacion, Usuario, UsuarioRol, Vista, TipoDocumento  # ✅ Importar solo lo necesario
from appgestor.Apis.serializers.serializer import \
    AmbienteSerializer, CompetenciaSerializer, EnviarCodigoSerializer, InstructorSerializer, ModuloSerializer, NivelFormacionSerializer, PeriodoSerializer, ProgramaSerializer,  RecuperarContrasenaSerializer, ResultadoAprendizajeSerializer, \
    RolSerializer, RolVistaSerializer, TipoDocumentoSerializer, TipoVinculacionSerializer, UsuarioLoginSerializer, UsuarioRolSerializer, \
    UsuarioSerializer, VerificarCodigoSerializer, VistaSerializer  # ✅ Importar explícitamente

class ModuloViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Modulo.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = ModuloSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Módulo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class VistaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Vista.objects.filter(fechaElimino__isnull=True)
    serializer_class = VistaSerializer

    def get_queryset(self):
        return VistaDAO.obtener_datos()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido

class RolVistaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = RolVista.objects.filter(fechaElimino__isnull=True)
    serializer_class = RolVistaSerializer

    def list(self, request):
        try:
            vistarol = RolVistaService.obtener_datos()  # Ahora sí recibe objetos DTO

            if not vistarol:
                return Response({'error': 'No hay contenido'}, status=status.HTTP_204_NO_CONTENT)

            # ✅ Ahora `asdict()` funcionará correctamente
            rolvista_dict = [asdict(rolvista) for rolvista in vistarol]
            return Response(rolvista_dict, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Rol vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class RolViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Rol.objects.filter(fechaElimino__isnull=True)
    serializer_class = RolSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Rol eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class UsuarioViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Usuario.objects.filter(fechaElimino__isnull=True)
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        """Sobrescribe el método create para usar UsuarioService."""
        data = request.data
        tipo_documento_id = data.get("tipoDocumento")  # Clave corregida

        # Convertir el ID en una instancia de TipoDocumento
        tipo_documento = get_object_or_404(TipoDocumento, id=tipo_documento_id)

        usuario = UsuarioService.crear(
            correo=data.get("correo"),
            nombres=data.get("nombres"),
            apellidos=data.get("apellidos"),
            documento=data.get("documento"),
            contrasena=data.get("contrasena"),
            tipoDocumento=tipo_documento,  # Pasamos la instancia
        )

        serializer = self.get_serializer(usuario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene el usuario actual
        data = request.data

        # Obtener el tipoDocumento de la solicitud o mantener el actual
        tipo_documento_id = data.get("tipoDocumento")
        tipo_documento = get_object_or_404(TipoDocumento, id=tipo_documento_id) if tipo_documento_id else instance.tipoDocumento

        usuario_actualizado = UsuarioService.actualizar(
            instance.id,
            correo=data.get("correo", instance.correo),
            nombres=data.get("nombres", instance.nombres),
            apellidos=data.get("apellidos", instance.apellidos),
            documento=data.get("documento", instance.documento),
            contrasena=data.get("contrasena") if "contrasena" in data else None,
            tipoDocumento=tipo_documento  # Mantenemos o actualizamos el tipo de documento
        )

        if usuario_actualizado:
            serializer = self.get_serializer(usuario_actualizado)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "No se pudo actualizar el usuario."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido

    @action(detail=False, methods=['get'])
    def usuario_sin_rol(self, request):
        usuarios_sin_rol = UsuarioService.listusuarios_sin_rol()

        if not usuarios_sin_rol:
            return Response({'message': 'No hay usuarios sin rol'}, status=status.HTTP_204_NO_CONTENT)

        return Response([usuario.__dict__ for usuario in usuarios_sin_rol], status=status.HTTP_200_OK)

    
class UsuarioRolViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = UsuarioRol.objects.filter(fechaElimino__isnull=True)
    serializer_class = UsuarioRolSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Usuario Rol eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class LoginView(APIView):

    @swagger_auto_schema(
        request_body=UsuarioLoginSerializer,
        responses={200: "Login exitoso", 400: "Credenciales inválidas", 403: "Usuario sin rol asignado"}
    )
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)

        if serializer.is_valid():
            correo = serializer.validated_data["correo"]
            contrasena = serializer.validated_data["contrasena"]

            usuario = UsuarioService.autenticar_usuario(correo, contrasena)

            if usuario:
                if not usuario.get("rol_id"):
                    return Response({"error": "Usuario sin rol asignado"}, status=status.HTTP_403_FORBIDDEN)

                return Response(usuario, status=status.HTTP_200_OK)

            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class RecuperarContrasenaViewSet(viewsets.GenericViewSet):  # ✅ Cambiado ModelViewSet
    queryset = RecuperarContrasena.objects.filter(usado=True)
    serializer_class = RecuperarContrasenaSerializer
    
    @swagger_auto_schema(
        request_body=EnviarCodigoSerializer, 
        responses={200: "Codigo enviado", 400: "Correo inválido"}
    )
    
    @action(detail=False, methods=["post"], url_path="enviar-codigo", url_name="enviar_codigo")
    def enviar_codigo(self, request):
        serializer = EnviarCodigoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        correo = request.data.get("correo")
        if not correo:  
            return Response({"error": "El correo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        resultado = RecuperarContrasenaService.EnviarCodigo(correo)

        if isinstance(resultado, str): 
            return Response({"error": resultado}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Código enviado correctamente", "usuario_id": resultado.usuario_id.id, "codigo": resultado.codigo}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=VerificarCodigoSerializer, 
        responses={200: "Código verificado", 400: "Código inválido"}
    )
    
    @action(detail=False, methods=["post"], url_path="verificar-codigo", url_name="verificar_codigo")
    def verificar_codigo(self, request):
        serializer = VerificarCodigoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        codigo = request.data.get("codigo")
        usuario_id = request.data.get("usuario_id")
        if not codigo or not usuario_id:
            return Response({"error": "El código y el usuario son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        resultado = RecuperarContrasenaService.VerificarCodigo(codigo, usuario_id)

        if isinstance(resultado, str):
            return Response({"error": resultado}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Código verificado correctamente"}, status=status.HTTP_200_OK)
    
    def destroy(self):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
    
class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.filter(fechaElimino__isnull=True)
    serializer_class = TipoDocumentoSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()

        return Response({'message':'Tipo de documento eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
    
    
### p
class InstructorViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Instructor.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = InstructorSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Instructor eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
    
class AmbienteViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Ambiente.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = AmbienteSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Ambiente eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
    
class PeriodoViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Periodo.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = PeriodoSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Periodo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
    
class NivelFormacionViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = NivelFormacion.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = NivelFormacionSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Nivel eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    

class TipoVinculacionViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = TipoVinculacion.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = TipoVinculacionSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Tipo de vinculo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    

class ProgramaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Programa.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = ProgramaSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Programa eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
    
class CompetenciaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Competencia.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = CompetenciaSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Competencia eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    

class ResultadoAprendizajeViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = ResultadoAprendizaje.objects.filter(fechaElimino__isnull=True)  # Filtra solo los activos
    serializer_class = ResultadoAprendizajeSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs, partial=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Resultado de aprendizaje eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)