from sqlalchemy import Table, Column, String
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
settings_table = sa.Table('settings',
                          Base.metadata,
                          sa.Column('id', String),
                          sa.Column('user_email', String),
                          sa.Column('aws_access_key', String),
                          sa.Column('aws_secret', String),
                          sa.Column('aws_region', String),
                          sa.Column('no_sql_provider', String),
                          sa.Column('document_table_name', String),
                          sa.Column('parsing_api_key', String),
                          )

# TODO : Add auto migrations from tables -> database