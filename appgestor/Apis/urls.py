from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appgestor.Apis.views.viewSet import LoginView, ModuloViewSet, \
    RecuperarContrasenaViewSet, RolViewSet, RolVistaViewSet, \
    UsuarioRolViewSet, UsuarioViewSet, VistaViewSet\

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'vistas', VistaViewSet, basename='vista')
router.register(r'rolvista', RolVistaViewSet, basename='rolvista')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'usuariorol', UsuarioRolViewSet, basename='usuariorol')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'recuperarcontrasena', RecuperarContrasenaViewSet, basename='recuperarcontrasena')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
