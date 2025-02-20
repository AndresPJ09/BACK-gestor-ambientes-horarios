from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appgestor.Apis.views.viewSet import AmbienteViewSet, InstructorViewSet, LoginView, ModuloViewSet, NivelFormacionViewSet, PeriodoViewSet, \
    RecuperarContrasenaViewSet, RolViewSet, RolVistaViewSet, TipoDocumentoViewSet, \
    UsuarioRolViewSet, UsuarioViewSet, VistaViewSet\

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'vistas', VistaViewSet, basename='vista')
router.register(r'rolvista', RolVistaViewSet, basename='rolvista')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'usuariorol', UsuarioRolViewSet, basename='usuariorol')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'tipodocumento', TipoDocumentoViewSet, basename='tipodocumento')
router.register(r'recuperarcontrasena', RecuperarContrasenaViewSet, basename='recuperarcontrasena')

#p
router.register(r'instructor', InstructorViewSet, basename='instructor')
router.register(r'ambiente', AmbienteViewSet, basename='ambiente')
router.register(r'nivelformacion', NivelFormacionViewSet, basename='nivelformacion')
router.register(r'periodo', PeriodoViewSet, basename='periodo')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
