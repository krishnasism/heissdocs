from sqlalchemy import create_engine, insert, update
import os
import logging
from .database.tables import settings_table
import re
from uuid import uuid4
from services.config import get_settings


SETTINGS_TABLE_NAME = 'settings'

CAMEL_TO_SNAKE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')


class PostgresManager():
    client = None
    settings = get_settings()

    def __init__(self):
        self._connect()

    def _convert_dict_to_snake_case(self, camel_dict: dict):
        snake_dict = {}
        for k, v in camel_dict.items():
            snake_dict[CAMEL_TO_SNAKE_PATTERN.sub('_', k).lower()] = v
        return snake_dict

    def _connect(self):
        connection_string = f"postgresql://{self.settings.postgres_username}:{self.settings.postgres_password}@{self.settings.postgres_endpoint}"
        try:
            self.client = create_engine(connection_string)
        except Exception as e:
            logging.exception("[PostgresSQL] Unable to connect")
            logging.error(e)

    def get_settings(self, user_email: str):
        with self.client.connect() as conn:
            result_set = conn.execute(settings_table.select().where(
                settings_table.c.user_email == user_email))
            result_row = result_set.first()
            return result_row._asdict() if result_row else {}

    def update_settings(self, settings: dict):
        settings = self._convert_dict_to_snake_case(settings)
        with self.client.connect() as conn:
            stored_settings = self.get_settings(settings['user_email'])
            if not stored_settings:
                settings['id'] = str(uuid4())
                statement = insert(settings_table).values(**settings)
            else:
                statement = update(settings_table).where(settings_table.c.user_email == settings['user_email']) \
                    .values(**settings)
            conn.execute(statement)
            conn.commit()
