from models import Pessoas, db_session

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Mariana', idade=9)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # filter_by retorna uma lista de obj
    # first(), consigo acessar exemplo: a idade da pessoa
    #pessoa = Pessoas.query.filter_by(nome='Mariana').first()
    #print(pessoa.idade)
    # necessário fazer um looping no filtro para retornar a busca
    # for p in pessoa:
    #     print(p)

# Altera dados na tabela pessoa
def altera_pessoa():
    #OBS: first() irá pegar o primeiro registro
    pessoa = Pessoas.query.filter_by(nome='Mariana').first()
    pessoa.idade = 21
    pessoa.save()
    print(pessoa.idade)

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Mariana').first()
    pessoa.delete()





if __name__ == '__main__':
    #insere_pessoas()
    #consulta()
    #altera_pessoa()
    exclui_pessoa()
    consulta()