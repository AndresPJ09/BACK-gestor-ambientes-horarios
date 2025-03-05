from dataclasses import dataclass
from datetime import datetime

@dataclass
class InstructorHorarioDTO:
    id=int
    dias: str
    horario_id: int
    jornada_programada: str
    hora_ingreso_horario: str
    hora_egreso_horario: str
    horas_horario: str
    instructor_id: int
    observaciones: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore