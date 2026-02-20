from models.database import Database
from datetime import datetime

with Database() as db:
    db.executar('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_tarefa TEXT NOT NULL,
            data_conclusao TEXT,           -- data prevista
            concluida BOOLEAN DEFAULT 0,
            data_conclusao_real TEXT       -- data/hora real que foi concluída
        )
    ''')
    print("Tabela tarefas criada/atualizada com sucesso!")