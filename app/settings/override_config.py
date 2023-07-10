from services.local.postgres import PostgresManager


def get_override_settings(user_email: str) -> dict:
    """
    Get override settings for a user from Postgres
    params: user_email: User email
    return: dict: settings for user
    """
    if user_email:
        pm = PostgresManager()
        override_settings = pm.get_settings(user_email)
        return override_settings
    else:
        return {}
