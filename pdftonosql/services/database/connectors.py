# Add all connectors for various database
import logging
from databases import Databases


class DatabaseConnection():
    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self.connect_to_mongodb()
            case _:
                logging.error("Undefined")

    def connect_to_mongodb(self):
        pass
