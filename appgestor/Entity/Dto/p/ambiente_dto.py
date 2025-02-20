from dataclasses import dataclass
from datetime import datetime

@dataclass
class AmbienteDTO:
    id: int
    codigo: str
    nombre: str
    capacidad: int
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime | None # type: ignore
    fecha_elimino: datetime | None # type: ignore
