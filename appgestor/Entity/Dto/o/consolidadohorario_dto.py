from dataclasses import dataclass
from datetime import datetime


@dataclass
class ConsolidadoHorarioDTO:
    id: int
    usuario_id: int
    usuario_nombres: str
    programa_id: int
    programa_nombre: str
    nivel_formacion_id: int
    nivelformacion_nombre: str
    ficha_id: int
    ficha_codigo: str
    ambiente_id: int
    ambiente_codigo: str
    ambiente_nombre: str
    competencia_id: int
    competencia_nombre: str
    competencia_descripcion: str
    resultadoaprendizaje_id: int
    resultadoaprendizaje_descripcion: str
    resultadoaprendizaje_est_ideal_evaluacion: str
    actvidadfase_id: int
    actvidadfase_fecha_inicio_actividad: str
    actvidadfase_fecha_fin_actividad: str
    actvidadfase_numero_semanas: str
    instructor_id: int
    instructor_nombres: str
    instructor_apellidos: str
    jornada_programada: str
    horas: str
    observaciones: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore