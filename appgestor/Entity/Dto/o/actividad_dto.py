from dataclasses import dataclass

@dataclass
class ActividadDTO:
    id: int
    nombre: str
    proyectofase_id: int
    #proyecto_fase: str
    estado: bool
