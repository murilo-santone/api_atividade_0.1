# Column - para poder criar colunas
# Integer - poder falar que um tipo é inteiro
# String - poder criar colunas do tipo string
# ForeignKey - poder relacionar uma classe/tabela com a outra, OBS: Sempre utilizar o nome da tabela.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# criando uma sessão
# relationship - relacionar conforme nosso exemplo, a classe atividades com pessoas,
# OBS: utiliza-se o nome da classe
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# sqlite 3 /// > nome do banco, convert_unicode=True para não termos problemas com acentuações no bd
engine = create_engine('sqlite:///atividades.db', convert_unicode=True )
# sempre que for fazer conexão com o bd tem uma nova sessão
# autocommit=Flase para não commitar sozinho, binds=engine para poder saber qual o banco que vai fazer abrir a sessão
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
# default do sqlalchemy
#todo esse trecho é necessário para que se crie banco de dados com sqlite
# e para também para que conseguimos fazer alterações no banco e consultas, trabalhar com ORM de fato
Base = declarative_base()
Base.query = db_session.query_property()
# feito tudo isso acima, iremos criar uma tabela, tabelas são classes


class Pessoas(Base):
    # posso ter um nome na classe, mas na tabela irá vir o nome de pessoas
    # então consigo trabalhar com o nome de classe diferente com o nome da tabela
    __tablename__='pessoas'
    # coluna tipo inteiro com chave primaria
    id = Column(Integer, primary_key=True)
    # coluna tipo string tamanho 40, index=True - cria um indice para essa coluna e deixa a consulta mais rápida
    # quando a consulta for pelo nome
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    # quando fazer consulta do obj, ele vai mostrar a representação da classe, '__repr__'
    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    # adiciona o próprio objeto
    # ao commitar é só chamar este método
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    # uma chave estrangeira, é preciso relacionar classe atividades com classe pessoas
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    # desta forma reconhece que tem relacionamento de atividades com pessoas
    pessoa = relationship('Pessoas')

    def __repr__(self):
        return f'<Atividade {self.nome}>'

    # adiciona o próprio objeto
    # ao commitar é só chamar este método
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    #create_all - cria o banco de dados
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()