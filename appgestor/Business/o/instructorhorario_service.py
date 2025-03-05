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
                instructorhorario_id=item['instructorhorario_id'],
                instructor_dia=item['instructor_dia'],
                jornada_programada=item['jornada_programada'],
                fecha_inicio_hora_ingreso=item['fecha_inicio_hora_ingreso'],
                fecha_fin_hora_egreso=item['fecha_fin_hora_egreso'],
                horas=item['horas'],
                instructor_observaciones=item['instructor_observaciones'],

                usuario_id=item['usuario_id'],
                usuario_nombres=item['usuario_nombres'],

                programa_id=item['programa_id'],
                programa_nombre=item['programa_nombre'],

                nivel_id=item['nivel_id'],
                nivel_nombre=item['nivel_nombre'],

                ficha_id=item['ficha_id'],
                ficha_codigo=item['ficha_codigo'],

                ambiente_id=item['ambiente_id'],
                ambiente_codigo=item['ambiente_codigo'],
                ambiente_nombre=item['ambiente_nombre']
            )
            for item in query
        ]

    @staticmethod
    def obtener_horarios_por_instructor(instructor_id):
        return InstructorHorarioDAO.obtener_horario_por_instructor(instructor_id)
