from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class ActividadFaseDTO:
    id: int
    actividad_id: int
    fase_id: int
    fecha_inicio_actividad: date
    fecha_fin_actividad: date
    numero_semanas: int
    estado: bool
    
