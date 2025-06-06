from dataclasses import dataclass
from datetime import datetime

@dataclass
class InstructorHorarioDTO:
    id: int 
    dia: str  
    usuario_id: int
    usuario_nombres: str
    instructor_id: int
    instructor_nombres: str
    instructor_apellidos: str
    programa_id: int
    programa_nombre: str
    nivel_formacion_id: int
    nivelformacion_nombre: str
    ficha_id: int
    ficha_codigo: str
    ambiente_id: int
    ambiente_codigo: str
    ambiente_nombre: str
    instructor_jornada_programada: str
    instructor_fecha_inicio_hora_ingreso: datetime
    instructor_fecha_fin_hora_egreso: datetime
    instructor_horas: int
    observaciones: str 
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
