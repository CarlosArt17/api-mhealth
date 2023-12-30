import psycopg
import json

class PrePacientesConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname='mhealth' user='postgres' host='localhost' password='postgres'")
        except psycopg.OperationalError as err:
            print(err)
            if self.conn:
                self.conn.close()
    
    def read_all(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM preguntas_pacientes")
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM preguntas_pacientes WHERE id_paciente = %s", (id,))
                data = cur.fetchone()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return None

    def write(self, data):
        data_copy = data.copy()
        
        # Convierte campos relevantes a cadenas JSON
        for field in ['op_p8', 'op_p6', 'op_p7', 'op_rf_p8', 'op_p9', 'op_p10', 'op_p11', 'op_p12', 'op_p13', 'op_p15', 'op_p16', 'hallazgosop_p1']:
            if field in data_copy and isinstance(data_copy[field], dict):
                data_copy[field] = json.dumps(data_copy[field])

        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO preguntas_pacientes (id_paciente, sd_p8, op_p8, fr_p6, op_p6, fr_p7, op_p7, 
                        fr_p8, op_rf_p8, fr_p9, op_p9, fr_p10, op_p10, fr_11, op_p11, fr_p12, op_p12, fr_p13, 
                        op_p13, fr_p15, op_p15, fr_p16, op_p16, hallazgos_p1, hallazgosop_p1) 
                        VALUES (%(id_paciente)s, %(sd_p8)s, %(op_p8)s, %(fr_p6)s, %(op_p6)s, %(fr_p7)s, %(op_p7)s, 
                        %(fr_p8)s, %(op_rf_p8)s, %(fr_p9)s, %(op_p9)s, %(fr_p10)s, %(op_p10)s, %(fr_11)s, %(op_p11)s, %(fr_p12)s, %(op_p12)s, %(fr_p13)s,
                        %(op_p13)s, %(fr_p15)s, %(op_p15)s, %(fr_p16)s, %(op_p16)s, %(hallazgos_p1)s, %(hallazgosop_p1)s);
                        """, data_copy)
        self.conn.commit()
    
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE preguntas_pacientes SET id_pp = %(id_pp)s, id_paciente = %(id_paciente)s, sd_p8 = %(sd_p8)s, op_p8 = %(op_p8)s, fr_p6 = %(fr_p6)s, op_p6 = %(op_p6)s, fr_p7 = %(fr_p7)s, op_p7 = %(op_p7)s,
                        fr_p8 = %(fr_p8)s, op_rf_p8 = %(op_rf_p8)s, fr_p9 = %(fr_p9)s, op_p9 = %(op_p9)s, fr_p10 = %(fr_p10)s, op_p10 = %(op_p10)s, fr_11 = %(fr_11)s, op_p11 = %(op_p11)s, fr_p12 = %(fr_p12)s, op_p12 = %(op_p12)s, fr_p13 = %(fr_p13)s,
                        op_p13 = %(op_p13)s, fr_p15 = %(fr_p15)s, op_p15 = %(op_p15)s, fr_p16 = %(fr_p16)s, op_p16 = %(op_p16)s, hallazgos_p1 = %(hallazgos_p1)s, hallazgosop_p1 = %(hallazgosop_p1)s
                        WHERE id_paciente = %(id_paciente)s
                        """, data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM preguntas_pacientes WHERE id_pp = %s
            """, (id,))
        self.conn.commit()


    def __del__(self):
        if self.conn is not None:
            self.conn.close()