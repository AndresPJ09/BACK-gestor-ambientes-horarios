from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import InstructorHorario

class InstructorHorarioDAO(BaseDAO):
    model = InstructorHorario

    @staticmethod
    def obtener_lista_instructor_horario(instructor_id):
        with connection.cursor() as cursor:
            cursor.execute("""
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
                    H.jornada_programada AS horario_jornada,
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
                    PR.codigo AS programa_codigo, 
                    PR.nombre AS programa_nombre,

                    N.id AS nivel_id,
                    N.codigo AS nivel_codigo, 
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
                WHERE IH.instructor_id = %s;
            """, [instructor_id])

            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            
            return results  # Retornamos una lista en lugar de un solo diccionario
