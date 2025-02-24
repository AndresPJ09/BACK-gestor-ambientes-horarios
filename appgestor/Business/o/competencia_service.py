from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.competencia_dao import CompetenciaDAO
from appgestor.Entity.Dto.o.competencia_dto import CompetenciaDTO


class CompetenciaService(BaseService):
    dao=CompetenciaDAO
    model=CompetenciaDTO
    