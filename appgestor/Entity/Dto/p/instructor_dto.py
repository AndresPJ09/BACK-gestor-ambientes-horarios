from dataclasses import dataclass
import datetime


@dataclass
class InstructorDTO:
    id: int
    nombres: str
    apellidos: str
    foto: bytes
    identificacion: str
    tipo_contrato: str
    especialidad: str 
    correo: str
    fecha_inicio_y_hora_ingreso: datetime
    fecha_finalizacion_y_hora_egreso: datetime
    horas_asignadas: int
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore