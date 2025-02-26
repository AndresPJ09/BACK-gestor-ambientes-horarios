from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class FichaDTO:
    id: int
    codigo: str
    programa_id: int
    proyecto_id: int
    fecha_inicio: date
    fecha_fin: date
    fin_lectiva: date
    numero_semanas: int
    cupo: int
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime
    fecha_elimino: datetime
