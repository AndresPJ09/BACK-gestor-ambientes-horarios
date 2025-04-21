from django.db import connection
from appgestor.Entity.Dao.base_dao import BaseDAO
from appgestor.models import ConsolidadoAmbiente

class ConsolidadoAmbienteDAO(BaseDAO):
    model = ConsolidadoAmbiente

    @staticmethod
    def obtener_todos_los_ambientes():
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT 
    CA.id AS consolidado_ambiente_id,

    A.id AS ambiente_id,
    CONCAT(A.codigo, ' ', A.nombre) AS ambiente_codigo,
    A.estado AS ambiente_activo,

    F.id AS ficha_id,
    F.codigo AS ficha_codigo,

    U.id AS usuario_id,
    CONCAT(U.nombres, ' ', U.apellidos) AS usuario_nombre_completo,

    I.id AS instructor_id,
    CONCAT(I.nombres, ' ', I.apellidos) AS instructor_nombre_completo,

    PR.id AS programa_id,
    PR.nombre AS programa_nombre,

    NF.id AS nivel_formacion_id,
    NF.nombre AS nivelformacion_nombre,

    CA.observaciones,
    CA.estado AS estado_consolidado,
    CA.fechaCreo AS fecha_creo,
    CA.fechaModifico AS fecha_modifico,
    CA.fechaElimino AS fecha_elimino,

    CASE 
        WHEN A.estado = FALSE THEN 'Inactivo'
        WHEN CA.id IS NOT NULL THEN 'Ocupado'
        ELSE 'Disponible'
    END AS estado

FROM ambiente A
LEFT JOIN consolidadoambiente CA ON CA.ambiente_id_id = A.id AND CA.fechaElimino IS NULL
LEFT JOIN horario H ON CA.horario_id_id = H.id  -- Ya no depende de estado TRUE
LEFT JOIN usuario U ON H.usuario_id_id = U.id
LEFT JOIN instructor I ON H.instructor_id_id = I.id
LEFT JOIN ficha F ON H.ficha_id_id = F.id
LEFT JOIN programa PR ON F.programa_id_id = PR.id
LEFT JOIN nivelformacion NF ON PR.nivel_formacion_id_id = NF.id

        """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result
