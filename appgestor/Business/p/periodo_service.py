from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.periodo_dao import PeriodoDAO
from appgestor.Entity.Dto.p.periodo_dto import PeriodoDTO


class PeriodoService(BaseService):
    dao=PeriodoDAO
    model=PeriodoDTO
    