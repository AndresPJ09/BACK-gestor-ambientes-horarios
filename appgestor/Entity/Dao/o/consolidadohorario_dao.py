from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import ConsolidadoHorario

class ConsolidadoHorarioDAO(BaseDAO):
    model = ConsolidadoHorario
    
    @staticmethod
    def obtener_todos_los_consolidados():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                CH.id AS consolidado_horario_id,
        
                CONCAT(U.nombres, ' ', U.apellidos) AS usuario_nombre_completo,
    
                PR.id AS programa_id,
                PR.nombre AS programa_nombre,
    
                NF.id AS nivel_formacion_id,
                NF.nombre AS nivelformacion_nombre,
    
                F.id AS ficha_id,
                F.codigo AS ficha_codigo,
    
                A.id AS ambiente_id,
                A.codigo AS ambiente_codigo, 
                A.nombre AS ambiente_nombre,
    
                C.id AS competencia_id,
                C.descripcion AS competencia_descripcion,
    
                RAP.id AS resultadoaprendizaje_id,
                RAP.descripcion AS resultadoaprendizaje_descripcion,
                RAP.est_ideal_evaluacion AS resultadoaprendizaje_est_ideal_evaluacion,
    
                AF.id AS actividadfase_id,
                AF.fecha_inicio_actividad AS actividadfase_fecha_inicio_actividad, 
                AF.fecha_fin_actividad AS actividadfase_fecha_fin_actividad,
                AF.numero_semanas AS actividadfase_numero_semanas,
    
	            I.id AS instructor_id,
                CONCAT(I.nombres, ' ', I.apellidos) AS instructor_nombre_completo,
    
                H.id AS horario_id,
                H.jornada_programada AS horario_jornada_programada,
                H.horas AS horario_horas

            FROM consolidadohorario CH
                INNER JOIN horario H ON CH.horario_id_id = H.id
                LEFT JOIN usuario U ON H.usuario_id_id = U.id
                LEFT JOIN instructor I ON H.instructor_id_id = I.id
                LEFT JOIN ficha F ON H.ficha_id_id = F.id
                LEFT JOIN programa PR ON F.programa_id_id = PR.id
                LEFT JOIN nivelformacion NF ON PR.nivel_formacion_id_id = NF.id
                LEFT JOIN ambiente A ON H.ambiente_id_id = A.id
                LEFT JOIN actividadfase AF ON F.proyecto_id_id = AF.id
                LEFT JOIN resultadoaprendizaje RAP ON AF.id = RAP.actividadfase_id_id
                LEFT JOIN competencia C ON RAP.competencia_id_id = C.id
            WHERE CH.fechaElimino IS NULL;
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result