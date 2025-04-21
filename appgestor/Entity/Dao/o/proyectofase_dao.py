from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import ProyectoFase

class ProyectoFaseDAO(BaseDAO):
    model = ProyectoFase
    
    
    @classmethod
    def obtener_proyecto_fase_nombre(cls):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                PF.id AS proyecto_fase_id,
                PRO.id AS proyecto_id,
                F.id AS fase_id,
                CONCAT(PRO.nombre, ' - ', F.nombre) AS proyecto_fase_nombre,
                PF.fechaCreo,
                PF.fechaModifico,
                PF.fechaElimino
                FROM 
                sena.ProyectoFase AS PF
                INNER JOIN
                sena.Proyecto AS PRO ON PF.proyecto_id_id = PRO.id
                INNER JOIN 
                sena.Fase AS F ON PF.fase_id_id = F.id
                WHERE 
                PF.fechaElimino IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
        