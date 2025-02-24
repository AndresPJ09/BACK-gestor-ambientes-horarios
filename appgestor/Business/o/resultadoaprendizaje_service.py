from appgestor.Business.base_service import BaseService
from appgestor.Entity.Dao.o.resultadoaprendizaje_dao import ResultadoAprendizajeDAO
from appgestor.Entity.Dto.o.resultadoaprendizaje_dto import ResultadoAprendizajeDTO


class ResultadoAprendizajeService(BaseService):
    dao=ResultadoAprendizajeDAO
    model=ResultadoAprendizajeDTO
    