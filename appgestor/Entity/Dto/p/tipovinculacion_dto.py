from dataclasses import dataclass

@dataclass
class TipoVinculacionDTO:
    id: int
    codigo: str
    nombre: str
    descripcion: str
    estado: bool
