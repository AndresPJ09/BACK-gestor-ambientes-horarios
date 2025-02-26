from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.consolidadoambiente_dao import ConsolidadoAmbienteDAO
from appgestor.Entity.Dto.o.consolidadoambiente_dto import ConsolidadoAmbienteDTO

class ConsolidadoAmbienteService(BaseService):
    dao=ConsolidadoAmbienteDAO
    model=ConsolidadoAmbienteDTO
    