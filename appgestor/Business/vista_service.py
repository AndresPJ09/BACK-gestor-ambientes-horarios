from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.vista_dao import VistaDAO
from appgestor.Entity.Dto.vista_dto import VistaDTO


class VistaService(BaseService):
    dao=VistaDAO
    model=VistaDTO