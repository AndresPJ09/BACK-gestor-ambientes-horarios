from dataclasses import dataclass
from datetime import datetime


@dataclass
class HorarioDTO:
    id=int
    usuario_id: int
    ficha_id: int
    ambiente_id: int
    periodo_id: int
    instructor_id: int
    jornada_programada: str
    fecha_inicio_hora_ingreso: datetime
    fecha_fin_hora_egreso: datetime
    horas: int
    validacion: str
    observaciones: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore