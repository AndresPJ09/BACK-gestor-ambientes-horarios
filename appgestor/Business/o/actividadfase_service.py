from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.activdadfase_dao import ActividadFaseDAO
from appgestor.Entity.Dto.o.actvidadfase_dto import ActividadFaseDTO


class ActividadFaseService(BaseService):
    dao=ActividadFaseDAO
    model=ActividadFaseDTO
    