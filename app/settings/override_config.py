from services.local.postgres import PostgresManager


def get_override_settings(user_email: str) -> dict:
    if user_email:
        pm = PostgresManager()
        override_settings = pm.get_settings(user_email)
        return override_settings
    else:
        return {}
