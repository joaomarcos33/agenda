<<<<<<< HEAD
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
=======
from sqlite3 import Connection, connect, Cursor
from types import Traceback
from typing import Optional, Self, Type
from typing import Any, Optional, Self, Type

class Database:
    def __init__(self, db_name: str) -> None :
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    def executa (self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    
    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self) -> None:
        self.connection.close()

    # Métodos para o gerenciamento de contexto

    #Método de entrada do contexto 
    def __enter__(self) -> self:
        return self

    # Método de saída do contexto 
    def __exit__(self, 
    exc_type, Optional[type[BaseException]],
    exc_value: Optional[BaseException], 
    tb: Optional[traceback]) -> None:

        print('exeção capturada no contexto:')
        print(f'Tipo: {exc_type.__name__}')
        print(f'mensagem: {exc_value}')
        print('Traceback completo')
        Traceback.print_tb(tb)

        self.close()


# Área de Testes
# try:
#     db = Database('./data/tarefas.sqlite3')
#     db.executar('''
#     CREATE TABLE IF NOT EXISTS tarefas (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         titulo_tarefa TEXT NOT NULL,
#         data_conclusao TEXT);
#     ''')
#     db.executar(" INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);", ("Estudar Python", "2026-01-29"))
# except Exception as e:
#     print(f"Erro ao criar tabela: {e}")
>>>>>>> 3fe41711b7def938ae64d9112b9f812fc570b108
