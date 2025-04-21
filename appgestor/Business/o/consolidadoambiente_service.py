from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.consolidadoambiente_dao import ConsolidadoAmbienteDAO
from appgestor.Entity.Dto.o.consolidadoambiente_dto import ConsolidadoAmbienteDTO

class ConsolidadoAmbienteService(BaseService):
    dao=ConsolidadoAmbienteDAO
    model=ConsolidadoAmbienteDTO

    @staticmethod
    def obtener_todos_los_ambientes():
        query = ConsolidadoAmbienteDAO.obtener_todos_los_ambientes()

        return [
            ConsolidadoAmbienteDTO(
                id=item.get('consolidado_ambiente_id'),
                
                ambiente_id=item.get('ambiente_id'),
                ambiente_codigo=item.get('ambiente_codigo'),
                
                ficha_id=item.get('ficha_id'),
                ficha_codigo=item.get('ficha_codigo'),
                
                usuario_id=item.get('usuario_id'),
                usuario_nombre_completo=item.get('usuario_nombre_completo'),
                
                instructor_id=item.get('instructor_id'),
                instructor_nombre_completo=item.get('instructor_nombre_completo'),
                
                programa_id=item.get('programa_id'),
                programa_nombre=item.get('programa_nombre'),
                
                nivel_formacion_id=item.get('nivel_formacion_id'),
                nivelformacion_nombre=item.get('nivelformacion_nombre'),
                
                observaciones=item.get('observaciones'),
                estado=item.get('estado'),
                
                fecha_creo=item.get('fecha_creo'),
                fecha_modifico=item.get('fecha_modifico'),
                fecha_elimino=item.get('fecha_elimino'),
                
            )
            for item in query
        ]


    