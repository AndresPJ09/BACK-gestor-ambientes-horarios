from dataclasses import dataclass
from datetime import datetime

@dataclass
class ConsolidadoAmbienteDTO:
    id: int
    ficha_id: int
    ambiente_id: int
    observaciones: str
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime
    fecha_elimino: datetime
