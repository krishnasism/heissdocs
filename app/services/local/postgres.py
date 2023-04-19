from sqlalchemy import create_engine
import os
import logging
from local.database.tables import settings_table

SETTINGS_TABLE_NAME = 'settings'


class PostgresManager():
    client = None

    def __init__(self):
        self._connect()

    def _connect(self):
        connection_string = f"postgres://{os.getenv('POSTGRES_USERNAME')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_ENDPOINT')}"
        try:
            self.client = create_engine(connection_string)
        except Exception as e:
            logging.exception("[PostgresSQL] Unable to connect")
            logging.error(e)

    def get_settings(self, user_id: str):
        with self.client.connect() as conn:
            result_set = conn.execute(settings_table.select().where(settings_table.c.userId==user_id))
            return result_set.first().__dict__

    def update_settings(self, user_id: str, settings: dict):
        pass
