from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.consolidadohorario_dao import ConsolidadoHorarioDAO
from appgestor.Entity.Dto.o.consolidadohorario_dto import ConsolidadoHorarioDTO


class ConsolidadoHorarioService(BaseService):
    dao=ConsolidadoHorarioDAO
    model=ConsolidadoHorarioDTO

    @staticmethod
    def obtener_todos_los_consolidados():
        query = ConsolidadoHorarioDAO.obtener_todos_los_consolidados()

        return [
            ConsolidadoHorarioDTO(
                id=item.get('consolidado_horario_id'),
                
                # Información de usuario
                usuario_id=item.get('usuario_id'),
                usuario_nombre_completo=item.get('usuario_nombre_completo'),
                
                # Información de programa y formación
                programa_id=item.get('programa_id'),
                programa_nombre=item.get('programa_nombre'),
                nivel_formacion_id=item.get('nivel_formacion_id'),
                nivelformacion_nombre=item.get('nivelformacion_nombre'),
                
                # Información de ficha
                ficha_id=item.get('ficha_id'),
                ficha_codigo=item.get('ficha_codigo'),
                
                # Información de ambiente
                ambiente_id=item.get('ambiente_id'),
                ambiente_codigo=item.get('ambiente_codigo'),
                ambiente_nombre=item.get('ambiente_nombre'),
                
                # Información de competencia
                competencia_id=item.get('competencia_id'),
                competencia_descripcion=item.get('competencia_descripcion'),
                
                # Información de resultado de aprendizaje
                resultadoaprendizaje_id=item.get('resultadoaprendizaje_id'),
                resultadoaprendizaje_descripcion=item.get('resultadoaprendizaje_descripcion'),
                resultadoaprendizaje_est_ideal_evaluacion=item.get('resultadoaprendizaje_est_ideal_evaluacion'),
                
                # Información de actividad fase
                actividadfase_id=item.get('actividadfase_id'),
                actividadfase_fecha_inicio_actividad=item.get('actividadfase_fecha_inicio_actividad'),
                actividadfase_fecha_fin_actividad=item.get('actividadfase_fecha_fin_actividad'),
                actividadfase_numero_semanas=item.get('actividadfase_numero_semanas'),
                
                # Información de instructor
                instructor_id=item.get('instructor_id'),
                instructor_nombre_completo=item.get('instructor_nombre_completo'),
                
                # Información de horario
                horario_id=item.get('horario_id'),
                horario_jornada_programada=item.get('horario_jornada_programada'),
                horario_horas=item.get('horario_horas'),
                
                # Campos de estado y fechas
                observaciones=item.get('observaciones'),
                estado=item.get('estado'),

            )
            for item in query
        ]