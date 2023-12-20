import verificacao

from models.tables import Aluno
from database import db
from flask import Blueprint, render_template,redirect, request, url_for



aluno_blueprint = Blueprint('alunos', __name__, template_folder='templates')

@aluno_blueprint.route('/cadastro', methods=['GET', 'POST'])
def inserir_aluno():
    if request.method == 'GET':
        return render_template('inserir_aluno.html')
        
    if request.method == 'POST':
        Nome = request.form.get('nome')
        Sexo = request.form.get('sexo')
        Cpf = request.form.get('cpf')
        Data_de_Nascimento = request.form.get('nascimento')
        Matricula = request.form.get('matricula')

        if not Nome or not Sexo or not Cpf or not Data_de_Nascimento or not Matricula:
            return "Todos os campos devem ser preenchidos"

        if not verificacao.verificar_cpf(Cpf):
            return "Cpf Inválido!"

        if not verificacao.verificar_dataNasc(Data_de_Nascimento):
            return "Data de nascimento Inválida!"

        if not verificacao.verificar_sexo(Sexo):
            return "Sexo Inválido!"

        if not verificacao.verificar_valor(Matricula):
            return "Matrícula Inválida!"

        if verificacao.existe_aluno(Cpf):
            return "O aluno já está cadastrado no sistema"
            
        if verificacao.existe_matricula(Matricula):
            return "A matrícula fornecida, pertence a outro aluno"

        
        u = Aluno(Nome, Sexo, Cpf, Data_de_Nascimento,Matricula)
        db.session.add(u)
        db.session.commit()

        
        return 'Dados cadastrados com sucesso!'



@aluno_blueprint.route('/listar')
def lista_alunos():
    alunos = Aluno.query.all()
    return render_template('listar_aluno.html', alunos = alunos)

@aluno_blueprint.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_aluno(id):
    a = Aluno.query.get(id)
    if request.method == 'GET':
        return render_template('atualizar_aluno.html', a = a)
    if request.method == 'POST':
        Nome = request.form.get('nome')
        Sexo = request.form.get('sexo')
        Cpf = request.form.get('cpf')
        Data_de_Nascimento = request.form.get('nascimento')
        Matricula = request.form.get('matricula')

        if not verificacao.verificar_cpf(Cpf):
            return "Cpf Inválido!"

        if not verificacao.verificar_dataNasc(Data_de_Nascimento):
            return "Data de nascimento Inválida!"

        if not verificacao.verificar_sexo(Sexo):
            return "Sexo Inválido!"

        if not verificacao.verificar_valor(Matricula):
            return "Matrícula Inválida!"

            
        a.Nome = Nome
        a.Sexo = Sexo
        a.Cpf = Cpf
        a.Data_de_Nascimento = Data_de_Nascimento
        a.Matricula = Matricula

        db.session.add(a)
        db.session.commit()
        return redirect('/aluno/listar')
        


@aluno_blueprint.route('/excluir/<int:id>', methods = ['GET', 'POST'])
def excluir_aluno(id):
    a = Aluno.query.get(id)
    if request.method == 'GET':
        return render_template('excluir_aluno.html', a = a)

    if request.method == 'POST':
        db.session.delete(a)
        db.session.commit()
        return 'Dados excluidos com sucesso!'



@aluno_blueprint.route('/buscador', methods = ['GET', 'POST'])
def buscar_aluno():
    if request.method == 'GET':
        return render_template('buscar_aluno.html')
    
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        aluno = verificacao.existe_aluno(cpf)

        if aluno:

            return redirect(url_for('alunos.exibir_aluno', id = aluno.id))

        else:
            return "Aluno nao encontrado!"

@aluno_blueprint.route('/buscador/<int:id>',methods = ['GET'])
def exibir_aluno(id):
    aluno = Aluno.query.get(id)

    return render_template('dados_aluno.html', aluno=aluno)



