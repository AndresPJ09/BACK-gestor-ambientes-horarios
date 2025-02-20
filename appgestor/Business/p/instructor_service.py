from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.instructor_dao import InstructorDAO
from appgestor.Entity.Dto.instrucutor_dto import InstructorDTO


class InstrcutorService(BaseService):
    dao=InstructorDAO
    model=InstructorDTO