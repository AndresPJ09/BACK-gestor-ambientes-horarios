from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.proyectofase_dao import ProyectoFaseDAO
from appgestor.Entity.Dto.o.proyectofase_dto import ProyectoFaseDTO

class ProyectoFaseService(BaseService):
    dao = ProyectoFaseDAO
    model = ProyectoFaseDTO
