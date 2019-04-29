from sqlalchemy.dialects.mssql import CHAR, NVARCHAR
from sqlalchemy.orm import relationship

from app import db


class City(db.Model):
    __tablename__ = 'Pessoas_Cidades'

    id = db.Column('ID', db.Integer(), primary_key=True)
    name = db.Column('Descricao', NVARCHAR(100), nullable=False)
    cep = db.Column('CEP', NVARCHAR(12), nullable=True)
    ibge_code = db.Column('CodIBGE', NVARCHAR(5), nullable=True)

    state_id = db.Column('EstadoID', db.Integer(), db.ForeignKey('Pessoas_Estados.ID'), nullable=False)
    state = relationship('State')


class State(db.Model):
    __tablename__ = 'Pessoas_Estados'

    id = db.Column('ID', db.Integer(), primary_key=True)
    name = db.Column('Descricao', NVARCHAR(50), nullable=False)
    federative_unity = db.Column('UF', CHAR(2), nullable=True)
    ibge_code = db.Column('CodIBGE', NVARCHAR(2), nullable=True)


"""
class Cidade(db.Model):
    __tablename__ = 'Pessoas_Cidades'

    ID = db.Column(db.Integer(), primary_key=True)
    Descricao = db.Column(NVARCHAR(100), nullable=False)
    CEP = db.Column(NVARCHAR(12), nullable=True)
    CodIBGE = db.Column(NVARCHAR(5), nullable=True)

    EstadoID = db.Column(db.Integer(), db.ForeignKey('Pessoas_Estados.ID'), nullable=False)
    Estado = relationship('Estado')


class Estado(db.Model):
    __tablename__ = 'Pessoas_Estados'

    ID = db.Column(db.Integer(), primary_key=True)
    Descricao = db.Column(NVARCHAR(50), nullable=False)
    UF = db.Column(CHAR(2), nullable=True)
    CodIBGE = db.Column(NVARCHAR(2), nullable=True)

    PaisID = db.Column(db.Integer(), nullable=True)
"""