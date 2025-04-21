from dataclasses import dataclass
from datetime import datetime

@dataclass
class ConsolidadoAmbienteDTO:
    id: int
    ambiente_id: int
    ambiente_codigo: str
    ficha_id: int
    ficha_codigo: str
    usuario_id: int
    usuario_nombre_completo: str
    instructor_id: int
    instructor_nombre_completo: str
    programa_id: int
    programa_nombre: str
    nivel_formacion_id: int
    nivelformacion_nombre: str
    observaciones: str
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime
    fecha_elimino: datetime
