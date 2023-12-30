from pydantic import BaseModel
from typing import Optional
import datetime

class PacienteSchema(BaseModel):
    fecha_nacimiento: datetime.date
    estado_civil: str
    escolaridad: str
    ciudad_nacimiento: str
    ciudad_residencia: str
    ocupacion: str
    edad_primer_menstruacion: int
    genero: bool
    id_re: int
    peso: float
    altura: float
    id_rimc: int
    frutasyverduras: int
    carnepescado: int
    legumbres: int
    comidachatarra: int
    bebidas: int
    dulces: int