<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, url_for
from models.database import Database
from models.tarefa import Tarefa

=======
from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa
>>>>>>> 3fe41711b7def938ae64d9112b9f812fc570b108
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

<<<<<<< HEAD
@app.route('/agenda', methods=['GET', 'POST'])
def agenda():
    if request.method == 'POST':
        titulo_tarefa = request.form.get('titulo-tarefa')
        data_conclusao = request.form.get('data-conclusao')
        if titulo_tarefa and data_conclusao:
            tarefa = Tarefa(titulo_tarefa, data_conclusao)
            tarefa.salvar_tarefa()
=======
@app.route('/agenda', methods=['GET','POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()
>>>>>>> 3fe41711b7def938ae64d9112b9f812fc570b108

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
<<<<<<< HEAD
    tarefa = Tarefa(None, None, idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    with Database() as db:
        query = "SELECT id, titulo_tarefa, data_conclusao, concluida, data_conclusao_real FROM tarefas WHERE id = ?"
        resultado = db.buscar_um(query, (idTarefa,))
        if not resultado:
            return redirect(url_for('agenda'))
        tarefa_selecionada = Tarefa(resultado[1], resultado[2], resultado[0], bool(resultado[3]), resultado[4])

    if request.method == 'POST':
        titulo = request.form.get('titulo-tarefa')
        data = request.form.get('data-conclusao')
        if titulo and data:
            tarefa = Tarefa(titulo, data, idTarefa)
            tarefa.atualizar_tarefas()
        return redirect(url_for('agenda'))

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html',
                           titulo=f'Editando tarefa ID {idTarefa}',
                           tarefa_selecionada=tarefa_selecionada,
                           tarefas=tarefas)

@app.route('/concluir/<int:idTarefa>')
def concluir(idTarefa):
    tarefa = Tarefa(None, None, idTarefa)
    tarefa.toggle_concluir()
    return redirect(url_for('agenda'))

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"

if __name__ == '__main__':
    print("Servidor Flask iniciado! Acesse http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
=======
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"
>>>>>>> 3fe41711b7def938ae64d9112b9f812fc570b108
