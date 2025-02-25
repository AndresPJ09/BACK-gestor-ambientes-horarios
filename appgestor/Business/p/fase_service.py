from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.p.fase_dao import FaseDAO
from appgestor.Entity.Dto.p.fase_dto import FaseDTO


class FaseService(BaseService):
    dao=FaseDAO
    model=FaseDTO
    