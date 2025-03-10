from dataclasses import dataclass
import datetime

@dataclass
class ActividadFaseDTO:
    id: int
    actividad_id: int
    fase_id: int
    fecha_inicio_actividad: datetime
    fecha_fin_actividad: datetime
    numero_semanas: datetime
    estado: bool
    
