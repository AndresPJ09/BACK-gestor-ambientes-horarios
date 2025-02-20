from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.ambiente_dao import AmbienteDAO
from appgestor.Entity.Dto.p.ambiente_dto import AmbienteDTO


class AmbienteService(BaseService):
    dao=AmbienteDAO
    model=AmbienteDTO
    