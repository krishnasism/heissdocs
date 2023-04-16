import psycopg2
import os
import logging


class PostgresManager():
    client = None

    def __init__(self):
        self._connect()

    def _connect(self):
        try:
            self.client = psycopg2.connect(
                host=os.getenv('POSTGRES_ENDPOINT'),
                database=os.getenv('POSTGRES_DB_NAME'),
                user=os.getenv('POSTGRES_USERNAME'),
                password=os.getenv('POSTGRES_PASSWORD')
            )
        except Exception as e:
            logging.exception("[PostgresSQL] Unable to connect")
            logging.error(e)

    def get_settings(self, user_id="local_user"):
        return {}

    def update_settings(self, user_id="local_user"):
        return True
