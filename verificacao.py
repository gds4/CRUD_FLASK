from datetime import date

from models.tables import Aluno


def verificar_valor(valor):
    if valor.isdigit() is True:
        return True
    else:
        return False


def verificar_sexo(string):
    if len(string) != 1:
        return False

    if string[0] != 'M' and string[0] != 'F':
        return False

    return True


def ano_bissexto(ano):

    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def verificar_dataNasc(string):
    elementos = string.split('/')

    if len(elementos) != 3:
        return False

    for i in range (3):
        if elementos[i].isdigit() is False:
            return False

    dia = int(elementos[0])
    mes = int(elementos[1])
    ano = int(elementos[2])

    ano_min = date.today().year - 100
    if ano < ano_min or ano > date.today().year:
        return False

    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if dia < 1 or dia > 31:
                return False

        case 4 | 6 | 9 | 11:
            if dia < 1 or dia > 30:
                return False

        case 2:
            if(ano_bissexto(ano) is True):
                if dia < 1 or dia > 29:
                    return False
            else:
                if dia < 1 or dia > 28:
                    return False
        case _:
            return False

    return True


def digito_verificador(cpf):

    peso = 10
    somatorio = 0
    cpf_array = [0] * 11

    for i in range (11):
        cpf_array[i]= int(cpf[i])

    for j in range (9):
        somatorio += cpf_array[j]*peso
        peso -= 1

    resto = somatorio % 11

    if 11 - resto > 9: 
        if cpf_array[9] != 0:
            return False
    else:
        if cpf_array[9] != 11 - resto:
            return False

    somatorio = 0
    peso = 11

    for k in range (10):
        somatorio += cpf_array[k]*peso
        peso -= 1

    resto = somatorio % 11

    if 11 - resto > 9: 
        if cpf_array[10] != 0:
            return False
    else:
        if cpf_array[10] != 11 - resto:
            return False

    return True


def verificar_cpf(cpf):
    if len(cpf) != 11:
        return False

    if cpf.isdigit() is False:
        return False

    if digito_verificador(cpf) is False:
        return False

    return True

def existe_aluno(cpf):
    aluno = Aluno.query.filter(Aluno.Cpf == cpf).first()

    if aluno:
        return aluno
    else:
        return None

def existe_matricula(matricula):
    aluno = Aluno.query.filter(Aluno.Matricula == matricula).first()

    if aluno:
        return aluno
    else:
        return None