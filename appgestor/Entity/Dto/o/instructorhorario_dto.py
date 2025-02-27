from dataclasses import dataclass
from datetime import datetime

@dataclass
class InstructorHorarioDTO:
    id=int
    dias: str
    horario_id: int
    instructor_id: int
    observaciones: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore