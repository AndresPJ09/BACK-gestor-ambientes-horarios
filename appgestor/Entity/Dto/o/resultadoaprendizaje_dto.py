from dataclasses import dataclass

@dataclass
class ResultadoAprendizajeDTO:
    id: int
    descripcion: str
    competencia_id: int
    est_ideal_evaluacion: str
    estado: bool
