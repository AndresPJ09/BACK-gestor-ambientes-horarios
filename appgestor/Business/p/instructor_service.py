from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.instructor_dao import InstructorDAO
from appgestor.Entity.Dto.p.instructor_dto import InstructorDTO


class InstrcutorService(BaseService):
    dao=InstructorDAO
    model=InstructorDTO