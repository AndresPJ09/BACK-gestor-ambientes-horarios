from dataclasses import dataclass

@dataclass
class ProyectoDTO:
    id: int
    nombre: str
    jornada_tecnica: str
    estado: bool
