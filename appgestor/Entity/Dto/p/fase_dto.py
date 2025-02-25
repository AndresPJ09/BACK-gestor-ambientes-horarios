from dataclasses import dataclass

@dataclass
class FaseDTO:
    id: int
    nombre: str
    descripcion: str
    estado: bool
