from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.proyecto_dao import ProyectoDAO
from appgestor.Entity.Dto.p.proyecto_dto import ProyectoDTO


class ProyectoService(BaseService):
    dao=ProyectoDAO
    model=ProyectoDTO
    