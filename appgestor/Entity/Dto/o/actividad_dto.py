from dataclasses import dataclass

@dataclass
class ActividadDTO:
    id: int
    nombre: str
    proyectofase_id: int
    #proyecto_nombre: str = None
    #fase_descripcion: str = None
    estado: bool
