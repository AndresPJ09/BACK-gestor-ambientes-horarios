from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.rolvista_dao import RolVistaDAO
from appgestor.Entity.Dto.rolVista_dto import RolVistaDTO


class RolVistaService(BaseService):
    model=RolVistaDTO
    dao=RolVistaDAO
