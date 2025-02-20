from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.usuarioRol_dao import UsuarioRolDAO
from appgestor.Entity.Dto.usuarioRol_dto import UsuarioRolDTO


class UsuarioRolService(BaseService):
    model=UsuarioRolDTO
    dao=UsuarioRolDAO