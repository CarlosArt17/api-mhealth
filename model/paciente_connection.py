import psycopg

class PacienteConnection():
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
                cur.execute("SELECT * FROM pacientes")
                data = cur.fetchall()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id,))
                data = cur.fetchone()
                return data
        except psycopg.Error as e:
            print("Error en la consulta SELECT:", e)
            return None

    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO pacientes (fecha_nacimiento, estado_civil, escolaridad, ciudad_nacimiento,
                        ciudad_residencia, ocupacion, edad_primer_menstruacion, genero, id_re, peso, altura, id_rimc, frutasyverduras, carnepescado,
                        legumbres, comidachatarra, bebidas, dulces) VALUES (%(fecha_nacimiento)s, %(estado_civil)s, %(escolaridad)s, %(ciudad_nacimiento)s,
                        %(ciudad_residencia)s, %(ocupacion)s, %(edad_primer_menstruacion)s, %(genero)s, %(id_re)s, %(peso)s, %(altura)s, %(id_rimc)s, %(frutasyverduras)s, %(carnepescado)s,
                        %(legumbres)s, %(comidachatarra)s, %(bebidas)s, %(dulces)s);
                        """, data)
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE pacientes SET fecha_nacimiento = %(fecha_nacimiento)s, estado_civil = %(estado_civil)s, escolaridad = %(escolaridad)s, ciudad_nacimiento = %(ciudad_nacimiento)s,
                        ciudad_residencia = %(ciudad_residencia)s, ocupacion = %(ocupacion)s, edad_primer_menstruacion = %(edad_primer_menstruacion)s, genero = %(genero)s, id_re = %(id_re)s, peso = %(peso)s, altura = %(altura)s, id_rimc = %(id_rimc)s, frutasyverduras = %(frutasyverduras)s, %(carnepescado)s,
                        legumbres = %(legumbres)s, comidachatarra = %(comidachatarra)s, bebidas = %(bebidas)s, dulces = %(dulces)s WHERE id_paciente = %(id_paciente)s
                        """, data)
        self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM pacientes WHERE id_paciente = %s
            """, (id,))
        self.conn.commit()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
