from pydantic import BaseModel


class LogRequest(BaseModel):
    user_email: str
    log_id: str
    log_level: str
    message: str
    created_on: str
    caller_filename: str
    caller_function_name: str
    caller_line_number: str
