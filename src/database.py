import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="garantia_notas",  # Substitua por garantia_notas ou o nome do seu banco de dados
            user="postgres",  # Substitua pelo seu usuário do PostgreSQL
            password="pedro2004",  # Substitua pela sua senha do PostgreSQL
            host="localhost",  # Substitua pelo host do seu PostgreSQL
            port="5432"  # Substitua pela porta do seu PostgreSQL
        )

    def consultar(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            return cur.fetchall()
        except Exception as e:
            print("Erro na consulta:", e)

    def executar(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print("Erro na execução:", e)
            self.conn.rollback()