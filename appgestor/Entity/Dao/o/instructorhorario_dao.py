from django.db import connection
from appgestor.models import InstructorHorario

class InstructorHorarioDAO:
    model = InstructorHorario

class InstructorHorarioDAO:
    @staticmethod
    def obtener_todos_los_horarios():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT IH.id AS instructor_horario_id,
                    IH.dia AS instructor_dia,
                    
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
                    
                    H.jornada_programada AS instructor_jornada_programada,
                    H.fecha_inicio_hora_ingreso AS instructor_fecha_inicio_hora_ingreso,
                    H.fecha_fin_hora_egreso AS instructor_fecha_fin_hora_egreso,
                    H.horas AS instructor_horas,
                    IH.observaciones AS instructor_observaciones

                    
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
    
    
    @staticmethod
    def obtener_horario_por_instructor(instructor_id):
        """Consulta los horarios filtrados por instructor_id."""
        query = """
            SELECT 
                IH.id AS instructor_horario_id,
                IH.dia AS instructor_dia,
                IH.observaciones AS instructor_observaciones,
                IH.estado AS instructor_estado,
                IH.fechaCreo AS instructor_fecha_creo,
                IH.fechaModifico AS instructor_fecha_modifico,
                IH.fechaElimino AS instructor_fecha_elimino,

                I.id AS instructor_id,
                I.nombres AS instructor_nombres,
                I.apellidos AS instructor_apellidos,

                H.id AS horario_id,
                H.fecha_inicio_hora_ingreso AS horario_hora_ingreso,
                H.fecha_fin_hora_egreso AS horario_hora_egreso, 
                H.horas AS horario_horas,
                H.jornada_programada AS horario_jornada_programada,
                H.observaciones AS horario_observaciones,

                U.id AS usuario_id,
                U.nombres AS usuario_nombres,

                P.id AS periodo_id,
                P.nombre AS periodo_nombre,
                P.fecha_inicio AS periodo_fecha_inicio,
                P.fecha_fin AS periodo_fecha_fin,
                P.ano AS periodo_ano,

                A.id AS ambiente_id,
                A.codigo AS ambiente_codigo, 
                A.nombre AS ambiente_nombre,

                F.id AS ficha_id,
                F.codigo AS ficha_codigo,

                PR.id AS programa_id,
                PR.nombre AS programa_nombre,

                N.id AS nivel_id,
                N.nombre AS nivel_nombre

            FROM sena.InstructorHorario AS IH
            INNER JOIN sena.Horario AS H ON IH.horario_id = H.id
            INNER JOIN sena.Ficha AS F ON H.ficha_id = F.id
            INNER JOIN sena.Programa AS PR ON F.programa_id = PR.id
            INNER JOIN sena.NivelFormacion AS N ON PR.nivel_formacion_id = N.id
            LEFT JOIN sena.Usuario AS U ON H.usuario_id = U.id
            LEFT JOIN sena.Instructor AS I ON IH.instructor_id = I.id
            LEFT JOIN sena.Ambiente AS A ON H.ambiente_id = A.id
            LEFT JOIN sena.Periodo AS P ON H.periodo_id = P.id
            WHERE IH.instructor_id = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [instructor_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results