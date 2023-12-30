from pydantic import BaseModel
from typing import Optional
import datetime

class PreguntasPacientesSchema(BaseModel):
    id_paciente: int
    sd_p8:  bool
    op_p8: dict
    fr_p6: bool
    op_p6: dict
    fr_p7: bool
    op_p7: dict
    fr_p8: bool
    op_rf_p8: dict
    fr_p9: bool
    op_p9: dict
    fr_p10: bool
    op_p10: dict
    fr_11: bool
    op_p11: dict
    fr_p12: bool
    op_p12: dict
    fr_p13: bool
    op_p13: dict
    fr_p15: bool
    op_p15: dict
    fr_p16: bool
    op_p16: dict
    hallazgos_p1: bool
    hallazgosop_p1: dict
