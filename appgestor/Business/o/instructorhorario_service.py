from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.instructorhorario_dao import InstructorHorarioDAO
from appgestor.Entity.Dto.o.instructorhorario_dto import InstructorHorarioDTO

class InstructorHorarioService(BaseService):
    dao = InstructorHorarioDAO
    model = InstructorHorarioDTO

    @staticmethod
    def obtener_todos_los_horarios():
        query = InstructorHorarioDAO.obtener_todos_los_horarios()

        return [
            InstructorHorarioDTO(
                id=item.get('instructor_horario_id'), 
                dia=item.get('instructor_dia'),

                usuario_id=item.get('usuario_id'),
                usuario_nombres=item.get('usuario_nombres'),
                
                instructor_id=item.get('instructor_id'),
                instructor_nombres=item.get('instructor_nombres'),
                instructor_apellidos=item.get('instructor_apellidos'),

                programa_id=item.get('programa_id'),
                programa_nombre=item.get('programa_nombre'),

                nivel_formacion_id=item.get('nivel_formacion_id'),  
                nivelformacion_nombre=item.get('nivelformacion_nombre'),  

                ficha_id=item.get('ficha_id'),
                ficha_codigo=item.get('ficha_codigo'),

                ambiente_id=item.get('ambiente_id'),
                ambiente_codigo=item.get('ambiente_codigo'),
                ambiente_nombre=item.get('ambiente_nombre'),
                
                instructor_jornada_programada=item.get('instructor_jornada_programada'),
                instructor_fecha_inicio_hora_ingreso=item.get('instructor_fecha_inicio_hora_ingreso'),
                instructor_fecha_fin_hora_egreso=item.get('instructor_fecha_fin_hora_egreso'),
                instructor_horas=item.get('instructor_horas'),
                observaciones=item.get('instructor_observaciones'),
            )
            for item in query
        ]
    
    @staticmethod
    def obtener_horario_por_usuario(usuario_id):
        query = InstructorHorarioDAO.obtener_horario_por_usuario(usuario_id)
        return [
            InstructorHorarioDTO(
                id=item.get('instructor_horario_id'),
                dia=item.get('instructor_dia'),
                
                usuario_id=item.get('usuario_id'),
                usuario_nombres=item.get('usuario_nombres'),
                
                instructor_id=item.get('instructor_id'),
                instructor_nombres=item.get('instructor_nombres'),
                instructor_apellidos=item.get('instructor_apellidos'),
                
                programa_id=item.get('programa_id'),
                programa_nombre=item.get('programa_nombre'),
                
                nivel_formacion_id=item.get('nivel_formacion_id'),  
                nivelformacion_nombre=item.get('nivelformacion_nombre'),  
                
                ficha_id=item.get('ficha_id'),
                ficha_codigo=item.get('ficha_codigo'),
                
                ambiente_id=item.get('ambiente_id'),
                ambiente_codigo=item.get('ambiente_codigo'),
                ambiente_nombre=item.get('ambiente_nombre'),
                
                instructor_jornada_programada=item.get('instructor_jornada_programada'),
                instructor_fecha_inicio_hora_ingreso=item.get('instructor_fecha_inicio_hora_ingreso'),
                instructor_fecha_fin_hora_egreso=item.get('instructor_fecha_fin_hora_egreso'),
                instructor_horas=item.get('instructor_horas'),
                observaciones=item.get('instructor_observaciones'),
            ) for item in query
        ]

    @staticmethod
    def obtener_horario_por_periodo(periodo_id):
        query = InstructorHorarioDAO.obtener_horario_por_periodo(periodo_id)
        return [
            InstructorHorarioDTO(
                id=item.get('instructor_horario_id'),
                dia=item.get('instructor_dia'),
                
                usuario_id=item.get('usuario_id'),
                usuario_nombres=item.get('usuario_nombres'),
                
                instructor_id=item.get('instructor_id'),
                instructor_nombres=item.get('instructor_nombres'),
                instructor_apellidos=item.get('instructor_apellidos'),
                
                programa_id=item.get('programa_id'),
                programa_nombre=item.get('programa_nombre'),
                
                nivel_formacion_id=item.get('nivel_formacion_id'),  
                nivelformacion_nombre=item.get('nivelformacion_nombre'),  
                
                ficha_id=item.get('ficha_id'),
                ficha_codigo=item.get('ficha_codigo'),
                
                ambiente_id=item.get('ambiente_id'),
                ambiente_codigo=item.get('ambiente_codigo'),
                ambiente_nombre=item.get('ambiente_nombre'),
                
                
                instructor_jornada_programada=item.get('instructor_jornada_programada'),
                instructor_fecha_inicio_hora_ingreso=item.get('instructor_fecha_inicio_hora_ingreso'),
                instructor_fecha_fin_hora_egreso=item.get('instructor_fecha_fin_hora_egreso'),
                instructor_horas=item.get('instructor_horas'),
                observaciones=item.get('instructor_observaciones'),
            ) for item in query
        ]