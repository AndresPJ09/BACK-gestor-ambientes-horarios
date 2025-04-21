from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class ActividadFaseDTO:
    id: int
    fecha_inicio_actividad: date
    fecha_fin_actividad: date
    numero_semanas: int
    actividad_id: int
    fase_id: int
    actividad_fase_nombre: str

    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
    
