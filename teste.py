from models.database import Database

with Database('./data/tarefas.sqlite3') as db:
    db.executar('insert into tarefas (titulo_tarefa, data_conclusao) values (?, ?);',
     ('usar o gerenciador de contexto', '2026-02-03')
     )