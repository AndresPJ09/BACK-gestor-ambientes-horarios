from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import ActividadFase

class ActividadFaseDAO(BaseDAO):
    model = ActividadFase

    @classmethod
    def obtener_actividad_fase_nombre(cls):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                AF.id AS actividad_fase_id,
                AF.fecha_inicio_actividad,
                AF.fecha_fin_actividad,
                AF.numero_semanas,
                A.id AS actividad_id,
                F.id AS fase_id,
                CONCAT(A.nombre, ' - ', F.nombre) AS actividad_fase_nombre,
                AF.fechaCreo,
                AF.fechaModifico,
                AF.fechaElimino
                FROM 
                sena.ActividadFase AS AF
                INNER JOIN
                sena.Actividad AS A ON AF.actividad_id_id = A.id
                INNER JOIN 
                sena.Fase AS F ON AF.fase_id_id = F.id
                WHERE 
                AF.fechaElimino IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return result
        