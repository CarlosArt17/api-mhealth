from pydantic import BaseModel
from typing import Optional
import datetime

class PreguntadosSchema(BaseModel):
    id_respuesta: int
    respuesta: bool
    dia: datetime.date
    hora: datetime.time    
    id_paciente: int