from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.Entity.Dto.tipodocumento_dto import TipoDocumentoDTO
from appgestor.models import TipoDocumento


class TipoDocumentoDAO(BaseDAO):
    model = TipoDocumento