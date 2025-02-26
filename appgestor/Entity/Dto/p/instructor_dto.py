from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class InstructorDTO:
    id: int
    nombres: str
    apellidos: str
    foto: Optional[bytes] 
    identificacion: str
    tipo_vinculacion_id: int
    especialidad: str 
    correo: str
    fecha_inicio: datetime
    fecha_finalizacion: datetime
    hora_ingreso: datetime.time
    hora_egreso: datetime.time
    horas_asignadas: int
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore