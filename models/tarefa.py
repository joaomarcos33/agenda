<<<<<<< HEAD
from models.database import Database
from datetime import datetime

class Tarefa:
    def __init__(self, titulo_tarefa, data_conclusao, id_tarefa=None, concluida=False, data_conclusao_real=None):
        self.id_tarefa = id_tarefa
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao
        self.concluida = concluida
        self.data_conclusao_real = data_conclusao_real

    def salvar_tarefa(self):
        with Database() as db:
            query = """
                INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida)
                VALUES (?, ?, 0)
            """
            db.executar(query, (self.titulo_tarefa, self.data_conclusao))
            self.id_tarefa = db.cursor.lastrowid

    @classmethod
    def obter_tarefas(cls):
        with Database() as db:
            query = """
                SELECT id, titulo_tarefa, data_conclusao, concluida, data_conclusao_real 
                FROM tarefas 
                ORDER BY concluida ASC, id DESC
            """
            resultados = db.buscar_tudo(query)
            return [cls(titulo, data_prevista, id_, bool(concluida), data_real)
                    for id_, titulo, data_prevista, concluida, data_real in resultados]

    def excluir_tarefa(self):
        if self.concluida:
            print("Não é possível excluir tarefa concluída sem reabrir primeiro.")
            return False
        with Database() as db:
            query = "DELETE FROM tarefas WHERE id = ?"
            db.executar(query, (self.id_tarefa,))
        return True

    def atualizar_tarefas(self):
        with Database() as db:
            query = """
                UPDATE tarefas 
                SET titulo_tarefa = ?, data_conclusao = ? 
                WHERE id = ?
            """
            db.executar(query, (self.titulo_tarefa, self.data_conclusao, self.id_tarefa))

    def toggle_concluir(self):
        with Database() as db:
            if self.concluida:
                query = "UPDATE tarefas SET concluida = 0, data_conclusao_real = NULL WHERE id = ?"
                db.executar(query, (self.id_tarefa,))
                self.concluida = False
                self.data_conclusao_real = None
            else:
                agora = datetime.now().strftime('%d/%m/%Y %H:%M')
                query = "UPDATE tarefas SET concluida = 1, data_conclusao_real = ? WHERE id = ?"
                db.executar(query, (agora, self.id_tarefa))
                self.concluida = True
                self.data_conclusao_real = agora
        return self.concluida
=======

from sqlite3 import Cursor
from typing import Self, Any, Optional
from models.database import Database

class Tarefa:
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str], id_tarefa: int = None,)-> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa

    @classmethod
    def id(cls, id: int):
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            print(resultado)

            #desenpacotamento de coleção
            [[titulo, data]] = resultado

        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data)
        
    def salvar_tarefa(self: Self)-> None:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao)
            db.executar(query, params)

    @classmethod
    def id(cls, id: int) -> Self:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultados: list[Any] = db.buscar_tudo(query, params)
            if not resultados:
                return None
            [[titulo, data]] = resultados
        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data)

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'SELECT id, titulo_tarefa, data_conclusao FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            tarefas: list[Any] = [cls(titulo, data) for titulo, data in resultados]
            return tarefas
    
    def excluir_tarefa(self) -> Cursor:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
>>>>>>> 3fe41711b7def938ae64d9112b9f812fc570b108
