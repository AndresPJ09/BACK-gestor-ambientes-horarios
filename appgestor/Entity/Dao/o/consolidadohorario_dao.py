from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import ConsolidadoHorario

class ConsolidadoHorarioDAO(BaseDAO):
    model = ConsolidadoHorario
    
    
    @staticmethod
    def obtener_todos_los_horarios():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    IH.id AS instructor_horario_id,
                    IH.observaciones AS instructor_observaciones,
                    IH.estado AS instructor_estado,
                    IH.fechaCreo AS fechaCreo,
                    IH.fechaModifico AS fechaModifico,
                    IH.fechaElimino AS fechaElimino,

                    U.id AS usuario_id,
                    U.nombres AS usuario_nombres,

                    I.id AS instructor_id,
                    I.nombres AS instructor_nombres,
                    I.apellidos AS instructor_apellidos,

                    PR.id AS programa_id,
                    PR.nombre AS programa_nombre,

                    N.id AS nivel_formacion_id,
                    N.nombre AS nivelformacion_nombre,

                    F.id AS ficha_id,
                    F.codigo AS ficha_codigo,

                    A.id AS ambiente_id,
                    A.codigo AS ambiente_codigo, 
                    A.nombre AS ambiente_nombre,

                    H.dia AS instructor_dia,
                    H.jornada_programada AS instructor_jornada_programada,
                    H.fecha_inicio_hora_ingreso AS instructor_fecha_inicio_hora_ingreso,
                    H.fecha_fin_hora_egreso AS instructor_fecha_fin_hora_egreso,
                    H.horas AS instructor_horas

                FROM sena.InstructorHorario AS IH
                INNER JOIN sena.Horario AS H ON IH.horario_id_id = H.id
                INNER JOIN sena.Instructor AS I ON IH.instructor_id_id = I.id
                INNER JOIN sena.Ficha AS F ON H.ficha_id_id = F.id
                LEFT JOIN sena.Usuario AS U ON H.usuario_id_id = U.id
                LEFT JOIN sena.Programa AS PR ON F.programa_id_id = PR.id
                LEFT JOIN sena.NivelFormacion AS N ON PR.nivel_formacion_id_id = N.id
                LEFT JOIN sena.Ambiente AS A ON H.ambiente_id_id = A.id 
                WHERE IH.fechaElimino IS NULL 
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result