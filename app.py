from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.paciente_connection import PacienteConnection
from model.preguntados_connection import PreguntadosConnection
from model.prepacientes_connection import PrePacientesConnection
from schema.paciente_schema import PacienteSchema
from schema.preguntados_schema import PreguntadosSchema
from schema.preguntaspacientes_schema import PreguntasPacientesSchema

app = FastAPI()
conn = PacienteConnection()
conn2 = PreguntadosConnection()
conn3 = PrePacientesConnection()

@app.get("/")
def read_root():
    return {"message": "La aplicación FastAPI está en funcionamiento. Conexión exitosa."}

# Rutas para pacientes
@app.get("/api/pacientes", status_code=HTTP_200_OK)
def root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["fecha_nacimiento"] = data[1]
        dictionary["estado_civil"] = data[2]
        dictionary["escolaridad"] = data[3]
        dictionary["ciudad_nacimiento"] = data[4]
        dictionary["ciudad_residencia"] = data[5]
        dictionary["ocupacion"] = data[6]
        dictionary["edad_primer_menstruacion"] = data[7]
        dictionary["genero"] = data[8]
        dictionary["id_re"] = data[9]
        dictionary["peso"] = data[10]
        dictionary["altura"] = data[11]
        dictionary["id_rimc"] = data[12]
        dictionary["frutasyverduras"] = data[13]
        dictionary["carnepescado"] = data[14]
        dictionary["legumbres"] = data[15]
        dictionary["comidachatarra"] = data[16]
        dictionary["bebidas"] = data[17]
        dictionary["dulces"] = data[18]
        items.append(dictionary)
    return items

@app.get("/api/pacientes/{id}", status_code=HTTP_200_OK)
def get_one(id: int):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["fecha_nacimiento"] = data[1]
    dictionary["estado_civil"] = data[2]
    dictionary["escolaridad"] = data[3]
    dictionary["ciudad_nacimiento"] = data[4]
    dictionary["ciudad_residencia"] = data[5]
    dictionary["ocupacion"] = data[6]
    dictionary["edad_primer_menstruacion"] = data[7]
    dictionary["genero"] = data[8]
    dictionary["id_re"] = data[9]
    dictionary["peso"] = data[10]
    dictionary["altura"] = data[11]
    dictionary["id_rimc"] = data[12]
    dictionary["frutasyverduras"] = data[13]
    dictionary["carnepescado"] = data[14]
    dictionary["legumbres"] = data[15]
    dictionary["comidachatarra"] = data[16]
    dictionary["bebidas"] = data[17]
    dictionary["dulces"] = data[18]
    return dictionary

@app.post("/api/insert_pacientes", status_code=HTTP_201_CREATED)
def insert(paciente_data:PacienteSchema):
    data = paciente_data.dict()
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/api/update_pacientes/{id}", status_code=HTTP_204_NO_CONTENT)
def update(paciente_data:PacienteSchema, id: int):
    data = paciente_data.dict()
    data["id_paciente"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete("/api/delete_pacientes/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

# Rutas para preguntados
@app.get("/api/preguntados", status_code=HTTP_200_OK)
def root():
    items = []
    for data in conn2.read_all():
        dictionary = {}
        dictionary["id_respuesta"] = data[0]
        dictionary["respuesta"] = data[1]
        dictionary["dia"] = data[2]
        dictionary["hora"] = data[3]
        dictionary["id_paciente"] = data[4]
        items.append(dictionary)
    return items

@app.get("/api/preguntados/{id}", status_code=HTTP_200_OK)
def get_one(id: int):
    dictionary = {}
    data = conn2.read_one(id)
    dictionary["id_respuesta"] = data[0]
    dictionary["respuesta"] = data[1]
    dictionary["dia"] = data[2]
    dictionary["hora"] = data[3]
    dictionary["id_paciente"] = data[4]
    return dictionary

@app.post("/api/insert_preguntados", status_code=HTTP_201_CREATED)
def insert(preguntados_data:PreguntadosSchema):
    data = preguntados_data.dict()
    conn2.write(data)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/api/update_preguntados/{id}", status_code=HTTP_204_NO_CONTENT)
def update(preguntados_data:PreguntadosSchema, id: int):
    data = preguntados_data.dict()
    data["id_respuesta"] = id
    conn2.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete("/api/delete_preguntados/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn2.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)

# Rutas para preguntas_pacientes
@app.get("/api/preguntas_pacientes", status_code=HTTP_200_OK)
def root():
    items = []
    for data in conn3.read_all():
        dictionary = {}
        dictionary["id_pp"] = data[0]
        dictionary["id_paciente"] = data[1]
        dictionary["sd_p8"] = data[2]
        dictionary["op_p8"] = data[3]
        dictionary["fr_p6"] = data[4]
        dictionary["op_p6"] = data[5]
        dictionary["fr_p7"] = data[6]
        dictionary["op_p7"] = data[7]
        dictionary["fr_p8"] = data[8]
        dictionary["op_rf_p8"] = data[9]
        dictionary["fr_p9"] = data[10]
        dictionary["op_p9"] = data[11]
        dictionary["fr_p10"] = data[12]
        dictionary["op_p10"] = data[13]
        dictionary["fr_11"] = data[14]
        dictionary["op_p11"] = data[15]
        dictionary["fr_p12"] = data[16]
        dictionary["op_p12"] = data[17]
        dictionary["fr_p13"] = data[18]
        dictionary["op_p13"] = data[19]
        dictionary["fr_p15"] = data[20]
        dictionary["op_p15"] = data[21]
        dictionary["fr_p16"] = data[22]
        dictionary["op_p16"] = data[23]
        dictionary["hallazgos_p1"] = data[24]
        dictionary["hallazgosop_p1"] = data[25]
        items.append(dictionary)
    return items

@app.get("/api/preguntas_pacientes/{id}", status_code=HTTP_200_OK)
def get_one(id: int):
    dictionary = {}
    data = conn3.read_one(id)
    dictionary["id_pp"] = data[0]
    dictionary["id_paciente"] = data[1]
    dictionary["sd_p8"] = data[2]
    dictionary["op_p8"] = data[3]
    dictionary["fr_p6"] = data[4]
    dictionary["op_p6"] = data[5]
    dictionary["fr_p7"] = data[6]
    dictionary["op_p7"] = data[7]
    dictionary["fr_p8"] = data[8]
    dictionary["op_rf_p8"] = data[9]
    dictionary["fr_p9"] = data[10]
    dictionary["op_p9"] = data[11]
    dictionary["fr_p10"] = data[12]
    dictionary["op_p10"] = data[13]
    dictionary["fr_11"] = data[14]
    dictionary["op_p11"] = data[15]
    dictionary["fr_p12"] = data[16]
    dictionary["op_p12"] = data[17]
    dictionary["fr_p13"] = data[18]
    dictionary["op_p13"] = data[19]
    dictionary["fr_p15"] = data[20]
    dictionary["op_p15"] = data[21]
    dictionary["fr_p16"] = data[22]
    dictionary["op_p16"] = data[23]
    dictionary["hallazgos_p1"] = data[24]
    dictionary["hallazgosop_p1"] = data[25]
    return dictionary

@app.post("/api/insert_preguntas_pacientes", status_code=HTTP_201_CREATED)
def insert(preguntas_pacientes_data:PreguntasPacientesSchema):
    data = preguntas_pacientes_data.dict()
    conn3.write(data)
    return Response(status_code=HTTP_201_CREATED)

@app.put("/api/update_preguntas_pacientes/{id}", status_code=HTTP_204_NO_CONTENT)
def update(preguntas_pacientes_data:PreguntasPacientesSchema, id: int):
    data = preguntas_pacientes_data.dict()
    data["id_pp"] = id
    conn3.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete("/api/delete_preguntas_pacientes/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id: int):
    conn3.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)