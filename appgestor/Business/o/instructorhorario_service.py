from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.instructorhorario_dao import InstructorHorarioDAO
from appgestor.Entity.Dto.o.instructorhorario_dto import InstructorHorarioDTO


class InstructorHorarioService(BaseService):
    dao=InstructorHorarioDAO
    model=InstructorHorarioDTO
    
    @staticmethod
    def obtener_lista_instructor_horario(intructor_id):
        return InstructorHorarioDAO.obtener_lista_instructor_horario(intructor_id)