from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import Ficha, Horario

class HorarioDAO(BaseDAO):
    model = Horario
    
    
