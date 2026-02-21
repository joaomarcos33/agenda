from models.database import Database
from typing import Optional, Self, Any
from sqlite3 import Cursor

class Tarefa:
    """
    Classe para representar uma tarefa, com métodos para salvar, obter, excluir tarefas em um banco de dados usando a classe `Database`.
    """
    def __init__(self: Self, 
                 titulo_tarefa: Optional[str] = None, 
                 data_conclusao: Optional[str] = None, 
                 id_tarefa: Optional[int] = None, 
                 concluida: Optional[int] = 0) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa
        self.concluida: Optional[int] = concluida

    @classmethod
    def id(cls, id_tarefa: int) -> Self:
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, concluida FROM tarefas WHERE id = ?;'
            params: tuple = (id_tarefa,)
            resultado: tuple = db.buscar_um(query, params)
            if not resultado:
                raise ValueError(f"Tarefa com ID {id_tarefa} não encontrada")
            titulo, data_conclusao, concluida = resultado
        return cls(titulo_tarefa=titulo, data_conclusao=data_conclusao, id_tarefa=id_tarefa, concluida=concluida)

    def salvar_tarefa(self: Self) -> None:
        with Database() as db:
            query: str = "INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida) VALUES (?,?,?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.concluida)
            db.executar(query, params)
            self.id_tarefa = db.cursor.lastrowid  # Pega o ID gerado

    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        with Database() as db:
            query: str = 'SELECT id, titulo_tarefa, data_conclusao, concluida FROM tarefas;'
            resultados: list[tuple] = db.buscar_tudo(query)
            tarefas: list[Self] = [cls(titulo, data, id_, concluida) 
                                  for id_, titulo, data, concluida in resultados]
            return tarefas
        
    def excluir_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def completar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET concluida = 1 WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
        
    def atualizar_tarefa(self) -> Cursor:
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, concluida = 0 WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado