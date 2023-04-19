from sqlalchemy import Table, Column, String

settings_table = Table('settings',
                       Column('id', String),
                       Column('userId', String),
                       Column('awsAccessKey', String),
                       Column('awsSecret', String),
                       Column('awsRegion', String),
                       Column('noSqlProvider', String),
                       Column('documentTableName', String),
                       Column('parsingApiKey', String),
                )
