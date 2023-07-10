import os


def load_env_file():
    """Load environment variables from .env file"""
    with open(".env", "r") as env_file:
        file_content = env_file.read().split("\n")
        for line in file_content:
            if "=" not in line:
                continue
            key, value = line.split("=")
            os.environ[key] = value.replace('"', "").strip()
