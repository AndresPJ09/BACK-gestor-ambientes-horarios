from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.nivelformacion_dao import NivelFormacionDAO
from appgestor.Entity.Dto.p.nivelformacion_dto import NivelFormacionDTO


class NivelFormacionService(BaseService):
    dao=NivelFormacionDAO
    model=NivelFormacionDTO
    