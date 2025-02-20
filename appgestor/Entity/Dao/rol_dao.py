from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.Entity.Dto.rol_dto import RolDTO
from appgestor.models import Rol


class RolDAO(BaseDAO):
    model = Rol