
from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.actividad_dao import ActividadDAO
from appgestor.Entity.Dto.o.actividad_dto import ActividadDTO


class ActividadService(BaseService):
    dao=ActividadDAO
    model=ActividadDTO
    
    @staticmethod
    def listar_actividades_completas():
        return ActividadDAO.get_actividades_completas()