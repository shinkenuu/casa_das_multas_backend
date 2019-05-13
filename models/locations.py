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
