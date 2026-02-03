from flask import Flask, render_template, request
from models.tarefa import Tarefa

app = Flask(__name__)

# lista em memória (simples)
tarefas = []


@app.route('/')
def home():
    return render_template('home.html', titulo='Home')


@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        titulo_tarefa = request.form.get('titulo-tarefa')
        data_conclusao = request.form.get('data-conclusao')

        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefas.append(tarefa)

    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)
