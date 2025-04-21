from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.activdadfase_dao import ActividadFaseDAO
from appgestor.Entity.Dto.o.actvidadfase_dto import ActividadFaseDTO


class ActividadFaseService(BaseService):
    dao=ActividadFaseDAO
    model=ActividadFaseDTO

    @classmethod
    def obtener_actividad_fase_nombre(cls):
        query = ActividadFaseDAO.obtener_actividad_fase_nombre()

        return [
            ActividadFaseDTO(
                id=item.get('actividad_fase_id'),
                fecha_inicio_actividad=item.get('fecha_inicio_actividad'),
                fecha_fin_actividad=item.get('fecha_fin_actividad'),
                numero_semanas=item.get('numero_semanas'),
                actividad_id=item.get('actividad_id'),
                fase_id=item.get('fase_id'),
                actividad_fase_nombre=item.get('actividad_fase_nombre'),
                
                fechaCreo=item.get('fechaCreo'),
                fechaModifico=item.get('fechaModifico'),
                fechaElimino=item.get('fechaElimino')
            )
            for item in query
        ]

    