from dataclasses import dataclass
from datetime import datetime

@dataclass
class ConsolidadoAmbienteDTO:
    id: int
    ambiente_id: int
    ambiente_codigo: str
    ambiente_nombre: str
    ficha_id: int
    ficha_codigo: str
    usuario_id: int
    usuario_nombres: str
    instructor_id: int
    instructor_nombres: str
    instructor_apellidos: str
    programa_id: int
    programa_nombre: str
    nivel_formacion_id: int
    nivelformacion_nombre: str
    observaciones: str
    estado: bool
    fecha_creo: datetime
    fecha_modifico: datetime
    fecha_elimino: datetime
