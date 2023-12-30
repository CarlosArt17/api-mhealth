import psycopg

class PreguntadosConnection():
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
                cur.execute("SELECT * FROM preguntados")
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return []
        
    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM preguntados WHERE id_paciente = %s", (id,))
                data = cur.fetchone()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return None
    
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO preguntados (id_respuesta, respuesta, dia, hora,
                        id_paciente) VALUES (%(id_respuesta)s, %(respuesta)s, %(dia)s, %(hora)s, %(id_paciente)s);
                        """, data)
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE preguntados SET id_respuesta = %(id_respuesta)s, respuesta = %(respuesta)s, dia = %(dia)s, hora = %(hora)s, id_paciente = %(id_paciente)s 
                WHERE id_respuesta = %(id_respuesta)s
                        """, data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM preguntados WHERE id_respuesta = %s
            """, (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()