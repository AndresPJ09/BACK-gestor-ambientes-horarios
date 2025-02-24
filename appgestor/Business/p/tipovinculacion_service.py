from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.tipovinculacion_dao import TipoVinculacionDAO
from appgestor.Entity.Dto.p.tipovinculacion_dto import TipoVinculacionDTO


class TipoVinculacionService(BaseService):
    dao=TipoVinculacionDAO
    model=TipoVinculacionDTO
    