from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.instructorhorario_dao import InstructorHorarioDAO
from appgestor.Entity.Dto.o.instructorhorario_dto import InstructorHorarioDTO


class InstructorHorarioService(BaseService):
    dao=InstructorHorarioDAO
    model=InstructorHorarioDTO
    