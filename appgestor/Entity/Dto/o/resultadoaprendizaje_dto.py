from dataclasses import dataclass

@dataclass
class ResultadoAprendizajeDTO:
    id: int
    descripcion: str
    actividadfase_id: int
    competencia_id: int
    est_ideal_evaluacion: str
    estado: bool
