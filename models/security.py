from sqlalchemy.dialects.mssql import NVARCHAR

from app import db

DEFAULT_APP_MEMBERSHIP_ID = 1 # Master


class Membership(db.Model):
    __tablename__ = 'Security_Membership'

    id = db.Column('ID', db.Integer(), primary_key=True)
    username = db.Column('UserName', NVARCHAR(256), nullable=False)
    password = db.Column('Password', NVARCHAR(128), nullable=False)
    email = db.Column('Email', NVARCHAR(256), nullable=False)
