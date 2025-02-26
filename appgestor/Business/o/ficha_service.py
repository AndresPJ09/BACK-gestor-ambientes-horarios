from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.ficha_dao import FichaDAO
from appgestor.Entity.Dto.o.ficha_dto import FichaDTO


class FichaService(BaseService):
    dao=FichaDAO
    model=FichaDTO
    