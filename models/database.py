import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

class Database:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = os.getenv('DATABASE', './data/tarefas.sqlite3')
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    def executar(self, query, params=()):
        self.cursor.execute(query, params)

    def buscar_um(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def buscar_tudo(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()