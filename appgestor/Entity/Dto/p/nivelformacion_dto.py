from dataclasses import dataclass
from datetime import datetime

@dataclass
class NivelFormacionDTO:
    id: int
    codigo: str
    nombre: str
    duracion: datetime
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime | None # type: ignore
    fecha_elimino: datetime | None # type: ignore
