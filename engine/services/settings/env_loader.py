import os


def load_env_file():
    """Load environment variables from .env file"""
    with open(".env", "r") as env_file:
        file_content = env_file.read().split("\n")
        for line in file_content:
            if "=" not in line:
                continue
            kv = line.split("=", maxsplit=1)
            value = kv[1] if len(kv) == 2 else None
            os.environ[kv[0]] = value.replace('"', "").strip() if value else None
