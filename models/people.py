from sqlalchemy.dialects.mssql import BIT, DATETIME, DECIMAL, MONEY, NVARCHAR, NTEXT, UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.hybrid import hybrid_property

from app import db
from models.security import DEFAULT_APP_MEMBERSHIP_ID

_LEGAL_TYPE_CHOICES = ('FÍSICA, JURÍDICA')

_PARTNER_TYPE_CUSTOMER = 'CUSTOMER'
_PARTNER_TYPE_PROVIDER = 'PROVIDER'
_PARTNER_TYPE_COLLABORATOR = 'COLLABORATOR'


class Person(db.Model):
    __tablename__ = 'Pessoas_Pessoa'

    id = db.Column('ID', db.Integer, primary_key=True)
    legal_type = db.Column('FisicaJuridica', NVARCHAR(8), nullable=True)  # FÍSICA | JURÍDICA
    name = db.Column('NomeRazaoSocial', NVARCHAR(60), nullable=True)
    nickname = db.Column('apelidoFantasia', NVARCHAR(60), nullable=True)
    rg_ie = db.Column('RgIe', NVARCHAR(20), nullable=True)
    cpf_cnpj = db.Column('CpfCnpj', NVARCHAR(20), nullable=True)
    is_customer = db.Column('FlagCliente', BIT(), nullable=False, default=True)
    is_provider = db.Column('FlagFornecedor', BIT(), nullable=False, default=False)
    is_collaborator = db.Column('FlagColaborador', BIT(), nullable=False, default=False)
    is_transporter = db.Column('FlagTransportador', BIT(), nullable=False, default=False)
    FlagProdutorRural = db.Column(BIT(), nullable=False, default=False)

    public_name = db.Column('Logradouro', NVARCHAR(60), nullable=True)
    address_number = db.Column('Numero', NVARCHAR(10), nullable=True)
    neighborhood = db.Column('Bairro', NVARCHAR(60), nullable=True)
    address_reference = db.Column('PontoReferencia', NVARCHAR(60), nullable=True)
    zip_code = db.Column('Cep', NVARCHAR(20), nullable=True)

    phone_1 = db.Column('Telefone1', NVARCHAR(20), nullable=True)
    phone_2 = db.Column('Telefone2', NVARCHAR(20), nullable=True)
    fax = db.Column('Fax', NVARCHAR(20), nullable=True)
    cellphone = db.Column('Celular', NVARCHAR(20), nullable=True)
    contact_1 = db.Column('Contato1', NVARCHAR(60), nullable=True)
    contact_2 = db.Column('Contato2', NVARCHAR(60), nullable=True)
    email = db.Column('Email', NVARCHAR(80), nullable=True)
    email_nfe = db.Column('EmailNFe', NVARCHAR(80), nullable=True)

    birth_date = db.Column('DataNascimento', DATETIME(), nullable=True)
    ValorAluguel = db.Column(MONEY(), nullable=True)
    RendaAtual = db.Column(MONEY(), nullable=True)
    RendaConjuge = db.Column(MONEY(), nullable=True)
    FlagEnviaCobranca = db.Column(BIT(), nullable=False, default=False)
    LimiteCredito = db.Column(DECIMAL(10, 2), nullable=True)
    FlagOptanteSimplesEstadual = db.Column(BIT(), nullable=False, default=False)
    observation = db.Column('Observacao', NTEXT(), nullable=True)
    is_incomplete_data = db.Column('FlagDadosIncompletos', BIT(), nullable=False, default=False)

    uid = db.Column('UID', UNIQUEIDENTIFIER(), nullable=True)
    is_active = db.Column('FlagAtivo', BIT(), nullable=False, default=True)
    created_at = db.Column('CriadoEm', DATETIME(), nullable=True)  # DEFAULT (getdate())
    updated_at = db.Column('ModificadoEm', DATETIME(), nullable=True)  # DEFAULT (getdate())

    #  FKs
    created_by = db.Column('CriadoPor', db.Integer, db.ForeignKey('Security_Membership.ID'),
                           nullable=False, default=DEFAULT_APP_MEMBERSHIP_ID)
    updated_by = db.Column('ModificadoPor', db.Integer, db.ForeignKey('Security_Membership.ID'),
                           nullable=False, default=DEFAULT_APP_MEMBERSHIP_ID)

    city_id = db.Column('CidadeID', db.Integer, db.ForeignKey('Pessoas_Cidades.ID'), nullable=False)
    city = relationship('City')

    EmpresaID = db.Column(db.Integer, nullable=False, default=1)

    RotaGrupoID = db.Column(db.Integer, nullable=True, default=1)
    ProfissaoAtividadeID = db.Column(db.Integer, nullable=True, default=1)
    ConceitoID = db.Column(db.Integer, nullable=True, default=1)

    @hybrid_property
    def partner_types(self):
        return [
            partner_type
            for partner_type in [
                _PARTNER_TYPE_CUSTOMER if self.is_customer else None,
                _PARTNER_TYPE_PROVIDER if self.is_provider else None,
                _PARTNER_TYPE_COLLABORATOR if self.is_collaborator else None,
            ] if partner_type is not None
        ]

    def set_partner_types(self, partner_types: list):
        self.is_customer = _PARTNER_TYPE_CUSTOMER in partner_types
        self.is_provider = _PARTNER_TYPE_PROVIDER in partner_types
        self.is_collaborator = _PARTNER_TYPE_COLLABORATOR in partner_types

    @validates('legal_type')
    def validate_legal_type(self, column_name, column_value):
        assert column_value in _LEGAL_TYPE_CHOICES
        return column_value
