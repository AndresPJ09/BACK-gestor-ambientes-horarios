from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.programa_dao import ProgramaDAO
from appgestor.Entity.Dto.o.programa_dto import ProgramaDTO


class ProgramaService(BaseService):
    dao=ProgramaDAO
    model=ProgramaDTO
    