from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import Actividad

class ActividadDAO(BaseDAO):
    model = Actividad

    #@classmethod
    #def get_actividades_completas(cls):
    #    with connection.cursor() as cursor:
    #        cursor.execute("""
    #            SELECT 
    #                A.id,
    #                A.nombre,
    #                PF.id AS proyectofase_id,
    #                CONCAT(PRO.nombre, ' - ', F.nombre) AS proyecto_fase,
    #                A.estado,
    #                A.fechaCreo
    #            FROM 
    #               sena.actividad AS A
    #            INNER JOIN 
    #                sena.proyectofase AS PF ON A.proyectofase_id_id = PF.id
    #            INNER JOIN 
    #                sena.proyecto AS PRO ON PF.proyecto_id_id = PRO.id
    #            INNER JOIN 
    #                sena.fase AS F ON PF.fase_id_id = F.id
    #            WHERE 
    #                A.fechaElimino IS NULL;
    #        """)
    #        columns = [col[0] for col in cursor.description]
    #        return [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        