from database import db

class Aluno(db.Model):

    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key = True)
    Nome = db.Column(db.String(100))
    Sexo = db.Column(db.String(100))
    Cpf = db.Column(db.String(20))
    Data_de_Nascimento = db.Column(db.String(100))
    Matricula = db.Column(db.String(100))

    def __init__(self, Nome, Sexo, Cpf, Nasc, Matricula):
        self.Nome = Nome
        self.Sexo = Sexo
        self.Cpf = Cpf
        self.Data_de_Nascimento = Nasc
        self.Matricula = Matricula

    def __repr__(self):
        return "Aluno: {}".format(self.Nome)