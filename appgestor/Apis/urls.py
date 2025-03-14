from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appgestor.Apis.views.viewSet import ActividadFaseViewSet, ActividadViewSet, AmbienteViewSet, CompetenciaViewSet, ConsolidadoAmbienteViewSet, ConsolidadoHorarioViewSet, FaseViewSet, FichaViewSet, HorarioViewSet, InstructorHorarioViewSet, InstructorViewSet, LoginView, ModuloViewSet, NivelFormacionViewSet, PeriodoViewSet, ProgramaViewSet, ProyectoFaseViewSet, ProyectoViewSet, \
    RecuperarContrasenaViewSet, ResultadoAprendizajeViewSet, RolViewSet, RolVistaViewSet, TipoDocumentoViewSet, TipoVinculacionViewSet, \
    UsuarioRolViewSet, UsuarioViewSet, VistaViewSet

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
router.register(r'tipovinculo', TipoVinculacionViewSet, basename='tipovinculo')
router.register(r'proyecto',ProyectoViewSet, basename='Pproyecto')
router.register(r'fase', FaseViewSet, basename='fase')



#o
router.register(r'programa', ProgramaViewSet, basename='programa')
router.register(r'competencia', CompetenciaViewSet, basename='competencia')
router.register(r'resultadoaprendizaje', ResultadoAprendizajeViewSet, basename='resultadoaprendizaje')
router.register(r'ficha', FichaViewSet, basename='ficha')
router.register(r'consolidadoambiente', ConsolidadoAmbienteViewSet, basename='consolidadoambiente')
router.register(r'consolidadohorario', ConsolidadoHorarioViewSet, basename='consolidadohorario')
router.register(r'horario', HorarioViewSet, basename='horario')
router.register(r'instructorhorario', InstructorHorarioViewSet, basename='instructorhorario')
router.register(r'actividad', ActividadViewSet, basename='actividad')
router.register(r'proyectofase', ProyectoFaseViewSet, basename='proyectofase')
router.register(r'actividadfase', ActividadFaseViewSet, basename='actividadfase')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]
