from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.rol_dao import RolDAO
from appgestor.Entity.Dto.vista_dto import VistaDTO


class RolService(BaseService):
    dao=RolDAO
    model=VistaDTO