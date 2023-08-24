from sqlalchemy import create_engine, insert, update, and_, select, func
import math
import logging
from .database.tables import settings_table, documents_progress_table, logs_table
import re
from uuid import uuid4
from settings.config import get_settings
from datetime import datetime
from typing import Tuple


SETTINGS_TABLE_NAME = "settings"

CAMEL_TO_SNAKE_PATTERN = re.compile(r"(?<!^)(?=[A-Z])")


class PostgresManager:
    client = None

    def __init__(self):
        self.settings = get_settings()
        self.__connect()

    def _convert_dict_to_snake_case(self, camel_dict: dict):
        """
        Convert dict keys from camelCase to snake_case
        params: camel_dict: Dict with camelCase keys
        """
        snake_dict = {}
        for k, v in camel_dict.items():
            snake_dict[CAMEL_TO_SNAKE_PATTERN.sub("_", k).lower()] = v
        return snake_dict

    def __connect(self):
        connection_string = f"postgresql://{self.settings.postgres_username}:{self.settings.postgres_password}@{self.settings.postgres_endpoint}"
        try:
            self.client = create_engine(connection_string)
        except Exception as e:
            logging.exception("[PostgresSQL] Unable to connect")
            logging.error(e)

    def get_settings(self, user_email: str) -> dict:
        """
        Get settings for a user
        params: user_email: User email
        return: dict: Settings for the user
        """
        with self.client.connect() as conn:
            result_set = conn.execute(
                settings_table.select().where(settings_table.c.user_email == user_email)
            )
            result_row = result_set.first()
            return result_row._asdict() if result_row else {}

    def get_documents_progress_paged(
        self,
        user_email: str,
        page: int,
        per_page: int,
    ) -> Tuple[list, int]:
        """
        Get paged documents progress for a user
        params: user_email: User email
                page: Page number
                per_page: Number of items per page
        return: list: Paged documents progress for the user
        """
        with self.client.connect() as conn:
            query = documents_progress_table.select().where(
                documents_progress_table.c.user_email == user_email
            )

            total_rows = conn.scalar(select(func.count()).select_from(query))
            total_pages = math.ceil(total_rows / per_page)
            page = min(max(1, page), total_pages)

            result_set = conn.execute(
                query.order_by(documents_progress_table.c.updated_on.desc())
                .offset((page - 1) * per_page)
                .limit(per_page)
            )

            result_rows = result_set.all()
            return [row._asdict() for row in result_rows], total_pages

    def get_documents_progress(self, user_email: str, document_id=None) -> list:
        """
        Get documents progress for a user
        params: user_email: User email
        return: list: Documents progress for the user
        """
        with self.client.connect() as conn:
            if not document_id:
                result_set = conn.execute(
                    documents_progress_table.select()
                    .where(documents_progress_table.c.user_email == user_email)
                    .order_by(documents_progress_table.c.updated_on.desc())
                )
            else:
                result_set = conn.execute(
                    documents_progress_table.select()
                    .where(
                        and_(
                            documents_progress_table.c.user_email == user_email,
                            documents_progress_table.c.document_id == document_id,
                        )
                    )
                    .order_by(documents_progress_table.c.updated_on.desc())
                )
            result_row = result_set.all()
            return [row._asdict() for row in result_row]

    def update_settings(self, settings: dict) -> None:
        """
        Update settings for a user
        params: settings: Settings for the user
        """
        settings = self._convert_dict_to_snake_case(settings)
        with self.client.connect() as conn:
            stored_settings = self.get_settings(settings["user_email"])
            if not stored_settings:
                settings["id"] = str(uuid4())
                statement = insert(settings_table).values(**settings)
            else:
                statement = (
                    update(settings_table)
                    .where(settings_table.c.user_email == settings["user_email"])
                    .values(**settings)
                )
            conn.execute(statement)
            conn.commit()

    def create_documents_progress_entry(self, documents_progress: dict) -> None:
        """
        Create documents progress entry for a user
        params: documents_progress: Documents progress object for the user
        return: None
        """
        documents_progress = self._convert_dict_to_snake_case(documents_progress)
        documents_progress["id"] = str(uuid4())
        documents_progress["updated_on"] = datetime.utcnow()
        with self.client.connect() as conn:
            statement = insert(documents_progress_table).values(**documents_progress)
            conn.execute(statement)
            conn.commit()

    def update_documents_progress(self, documents_progress: dict) -> None:
        """
        Update documents progress for a user
        params: documents_progress: Documents progress object for the user
        return: None
        """
        documents_progress = self._convert_dict_to_snake_case(documents_progress)
        stored_documents_progress = self.get_documents_progress(
            documents_progress["user_email"], documents_progress["document_id"]
        )[0]
        with self.client.connect() as conn:
            pages_parsed = (
                documents_progress["pages_parsed"]
                if documents_progress["pages_parsed"]
                else stored_documents_progress["pages_parsed"]
            )
            if documents_progress["pages_parsed"]:
                pages_parsed += stored_documents_progress["pages_parsed"]

            # Lock the row for update
            result = conn.execute(
                documents_progress_table.select()
                .where(
                    and_(
                        documents_progress_table.c.user_email
                        == documents_progress["user_email"],
                        documents_progress_table.c.document_id
                        == documents_progress["document_id"],
                    )
                )
                .with_for_update()
            )
            row = result.fetchone()
            if row:
                statement = (
                    update(documents_progress_table)
                    .where(
                        and_(
                            documents_progress_table.c.user_email
                            == documents_progress["user_email"],
                            documents_progress_table.c.document_id
                            == documents_progress["document_id"],
                        )
                    )
                    .values(
                        **{
                            "stage": documents_progress["stage"]
                            if documents_progress["stage"]
                            else stored_documents_progress["stage"],
                            "pages_parsed": pages_parsed,
                            "total_pages": documents_progress["total_pages"]
                            if documents_progress["total_pages"]
                            else stored_documents_progress["total_pages"],
                            "updated_on": datetime.utcnow(),
                        }
                    )
                )
                conn.execute(statement)
                conn.commit()

    def post_log(self, log: dict) -> None:
        """
        Post log sent from parse engine
        params: log: Log sent from parse engine
        return: None
        """
        with self.client.connect() as conn:
            statement = insert(logs_table).values(**log)
            conn.execute(statement)
            conn.commit()

    def get_logs_paged(
        self,
        user_email: str,
        page: int,
        per_page: int,
    ) -> list:
        """
        Get all logs from the database.
        params: None
        return: list: A list of log dictionaries.
        """
        with self.client.connect() as conn:
            result_set = conn.execute(
                logs_table.select()
                .where(logs_table.c.user_email == user_email)
                .order_by(logs_table.c.created_on.desc())
                .offset((page - 1) * per_page)
                .limit(per_page)
            )
            result_rows = result_set.all()
            result_rows_safe = []
            for row in result_rows:
                row_safe = row._asdict()
                row_safe["created_on"] = row_safe["created_on"].strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                result_rows_safe.append(row_safe)
            total_logs = conn.scalar(select(func.count()).select_from(logs_table))
            total_pages = math.ceil(total_logs / per_page)
            return result_rows_safe, total_pages

    def get_logs_in_time_range_paged(
        self,
        user_email: str,
        start_datetime: datetime,
        end_datetime: datetime,
        page: int,
        per_page: int,
    ) -> list:
        with self.client.connect() as conn:
            result_set = conn.execute(
                logs_table.select()
                .where(
                    and_(
                        logs_table.c.user_email == user_email,
                        logs_table.c.created_on.between(start_datetime, end_datetime),
                    )
                )
                .order_by(logs_table.c.created_on.desc())
                .offset((page - 1) * per_page)
                .limit(per_page)
            )
            result_rows = result_set.all()
            result_rows_safe = []
            for row in result_rows:
                row_safe = row._asdict()
                row_safe["created_on"] = row_safe["created_on"].strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                result_rows_safe.append(row_safe)
            total_logs = conn.scalar(
                select(func.count())
                .select_from(logs_table)
                .where(
                    and_(
                        logs_table.c.user_email == user_email,
                        logs_table.c.created_on.between(start_datetime, end_datetime),
                    )
                )
            )
            # Calculate pagination information
            total_pages = math.ceil(total_logs / per_page)
            return result_rows_safe, total_pages
