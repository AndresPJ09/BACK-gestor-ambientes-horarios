from dataclasses import dataclass
from datetime import datetime

@dataclass
class ProyectoFaseDTO:
    
    id: int
    proyecto_id: int
    fase_id: int
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
