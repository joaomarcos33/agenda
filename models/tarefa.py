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