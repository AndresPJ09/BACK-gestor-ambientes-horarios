from dataclasses import dataclass

@dataclass
class ProgramaDTO:
    id: int
    codigo: str
    nombre: str
    nivel_formacion_id: int
    estado: bool
