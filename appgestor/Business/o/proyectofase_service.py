from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.proyectofase_dao import ProyectoFaseDAO
from appgestor.Entity.Dto.o.proyectofase_dto import ProyectoFaseDTO

class ProyectoFaseService(BaseService):
    dao = ProyectoFaseDAO
    model = ProyectoFaseDTO
    
    @classmethod
    def obtener_proyecto_fase_nombre(cls):
        query = ProyectoFaseDAO.obtener_proyecto_fase_nombre()

        return [
            ProyectoFaseDTO(
                id=item.get('proyecto_fase_id'),
                
                proyecto_id=item.get('proyecto_id'),
                fase_id=item.get('fase_id'),
                proyecto_fase_nombre=item.get('proyecto_fase_nombre'),
                
                fechaCreo=item.get('fechaCreo'),
                fechaModifico=item.get('fechaModifico'),
                fechaElimino=item.get('fechaElimino')
            )
            for item in query
        ]
