from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class PeriodoDTO:
    id: int
    nombre: str
    fecha_inicio: date
    fecha_fin: date
    ano: int
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime | None # type: ignore
    fecha_elimino: datetime | None # type: ignore
