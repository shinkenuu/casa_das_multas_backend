from sqlalchemy.dialects.mssql import BIT, DATETIME, DECIMAL, MONEY, NVARCHAR, NTEXT, UNIQUEIDENTIFIER

from app import db


class Pessoa(db.Model):
    __tablename__ = 'Pessoas_Pessoa'

    ID = db.Column(db.Integer, primary_key=True)  # [ID] [int] IDENTITY(1,1) NOT NULL,
    Bairro = db.Column(NVARCHAR(60), nullable=True)  # [Bairro] [nvarchar](60) NULL,
    FisicaJuridica = db.Column(NVARCHAR(8), nullable=True)  # FÍSICA | JURÍDICA - [FisicaJuridica] [nvarchar](8) NULL,
    NomeRazaoSocial = db.Column(NVARCHAR(60), nullable=True)  # [NomeRazaoSocial] [nvarchar](60) NULL,
    apelidoFantasia = db.Column(NVARCHAR(60), nullable=True)  # [ApelidoFantasia] [nvarchar](60) NULL,
    CpfCnpj = db.Column(NVARCHAR(20), nullable=True)  # no symbols, just digits - [CpfCnpj] [nvarchar](20) NULL,
    FlagCliente = db.Column(BIT(), nullable=False, default=True)  # [FlagCliente] [bit] NOT NULL,
    FlagFornecedor = db.Column(BIT(), nullable=False, default=False)  # [FlagFornecedor] [bit] NOT NULL,
    FlagColaborador = db.Column(BIT(), nullable=False, default=False)  # [FlagColaborador] [bit] NOT NULL,
    FlagTransportador = db.Column(BIT(), nullable=False, default=False)  # [FlagTransportador] [bit] NOT NULL,
    Logradouro = db.Column(NVARCHAR(60), nullable=True)  # [Logradouro] [nvarchar](60) NULL,
    Cep = db.Column(NVARCHAR(20), nullable=True)  # no symbols, just digits [Cep] - [nvarchar](10) NULL,
    Telefone1 = db.Column(NVARCHAR(20), nullable=True)  # no symbols, just digits - [Telefone1] [nvarchar](20) NULL,
    Telefone2 = db.Column(NVARCHAR(20), nullable=True)  # no symbols, just digits - [Telefone2] [nvarchar](20) NULL,
    Fax = db.Column(NVARCHAR(20), nullable=True)  # [Fax] [nvarchar](20) NULL,
    Celular = db.Column(NVARCHAR(20), nullable=True)  # [Celular] [nvarchar](20) NULL,
    Contato1 = db.Column(NVARCHAR(60), nullable=True)  # [Contato1] [nvarchar](60) NULL,
    Contato2 = db.Column(NVARCHAR(60), nullable=True)  # [Contato2] [nvarchar](60) NULL,
    Email = db.Column(NVARCHAR(80), nullable=True)  # [Email] [nvarchar](80) NULL,
    PontoReferencia = db.Column(NVARCHAR(60), nullable=True)  # [PontoReferencia] [nvarchar](60) NULL,
    DataNascimento = db.Column(DATETIME(), nullable=True)  # [DataNascimento] [datetime] NULL,
    ValorAluguel = db.Column(MONEY(), nullable=True)  # [ValorAluguel] [money] NULL,
    RendaAtual = db.Column(MONEY(), nullable=True)  # [RendaAtual] [money] NULL,
    RendaConjuge = db.Column(MONEY(), nullable=True)  # [RendaConjuge] [money] NULL,
    FlagEnviaCobranca = db.Column(BIT(), nullable=False, default=False)  # [FlagEnviaCobranca] [bit] NOT NULL,
    LimiteCredito = db.Column(DECIMAL(10, 2), nullable=True)  # [LimiteCredito] [decimal](10, 2) NULL,
    FlagOptanteSimplesEstadual = db.Column(BIT(), nullable=False,
                                           default=False)  # [FlagOptanteSimplesEstadual] [bit] NOT NULL,
    FlagProdutorRural = db.Column(BIT(), nullable=False, default=False)  # [FlagProdutorRural] [bit] NOT NULL,
    Observacao = db.Column(NTEXT(), nullable=True)  # [Observacao] [ntext] NULL,
    FlagDadosIncompletos = db.Column(BIT(), nullable=False, default=False)  # [FlagDadosIncompletos] [bit] NOT NULL,
    FlagAtivo = db.Column(BIT(), nullable=False, default=True)  # [FlagAtivo] [bit] NOT NULL,
    CriadoEm = db.Column(DATETIME(), nullable=True)  # [CriadoEm] [datetime] NULL, DEFAULT (getdate())
    ModificadoEm = db.Column(DATETIME(), nullable=True)  # [ModificadoEm] [datetime] NULL, DEFAULT (getdate())
    Numero = db.Column(NVARCHAR(10), nullable=True)  # [Numero] [nvarchar](10) NULL,
    UID = db.Column(UNIQUEIDENTIFIER(), nullable=True)  # [UID] [uniqueidentifier] NULL, DEFAULT (newid())
    EmailNFe = db.Column(NVARCHAR(80), nullable=True)  # [EmailNFe] [nvarchar](80) NULL,

    #  FKs
    CriadoPor = db.Column(db.Integer, db.ForeignKey('Security_Membership.ID'),
                          nullable=False)  # [CriadoPor] [int] NOT NULL, [Security_Membership]
    ModificadoPor = db.Column(db.Integer, db.ForeignKey('Security_Membership.ID'),
                              nullable=False)  # [ModificadoPor] [int] NOT NULL, [Security_Membership]

    EmpresaID = db.Column(db.Integer, db.ForeignKey('Pessoas_Empresas.ID'), nullable=False,
                          default=1)  # [EmpresaID] [int] NOT NULL,
    CidadeID = db.Column(db.Integer, db.ForeignKey('Pessoas_Cidades.ID'), nullable=False)  # [CidadeID] [int] NOT NULL,

    RotaGrupoID = db.Column(db.Integer, nullable=True, default=1)  # [RotaGrupoID] [int] NULL,
    ProfissaoAtividadeID = db.Column(db.Integer, nullable=True, default=1)  # [ProfissaoAtividadeID] [int] NULL,
    ConceitoID = db.Column(db.Integer, nullable=True, default=1)  # [ConceitoID] [int] NULL,
