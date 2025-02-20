from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.tipodocumento_dao import TipoDocumentoDAO
from appgestor.Entity.Dto.tipodocumento_dto import TipoDocumentoDTO


class TipoDocumentoService(BaseService):
    DAO = TipoDocumentoDAO
    model = TipoDocumentoDTO