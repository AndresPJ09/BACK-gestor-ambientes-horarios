from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.Entity.Dto.recuperarcontrasena_dto import RecuperarContrasenaDTO
from appgestor.models import RecuperarContrasena


class RecuperarContrasenaDAO(BaseDAO):
    model=RecuperarContrasena
    
    @classmethod
    def obtener_por_codigo(cls, codigo, usuario_id):
        return cls.model.objects.filter( codigo = codigo, usado = False, usuario_id = usuario_id).first()