CREATE TABLE IF NOT EXISTS logs (
    log_id VARCHAR PRIMARY KEY,
    user_email VARCHAR NOT NULL,
    log_level VARCHAR NOT NULL,
    message VARCHAR,
    created_on TIMESTAMP,
    caller_filename VARCHAR,
    caller_function_name VARCHAR,
    caller_line_number VARCHAR
)