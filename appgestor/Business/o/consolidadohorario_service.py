from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.horario_dao import HorarioDAO
from appgestor.Entity.Dto.o.horario_dto import HorarioDTO


class HorarioService(BaseService):
    dao=HorarioDAO
    model=HorarioDTO