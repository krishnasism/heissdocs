CREATE TABLE IF NOT EXISTS documents_progress (
    id VARCHAR PRIMARY KEY,
    user_email VARCHAR NOT NULL,
    document_id VARCHAR NOT NULL UNIQUE,
    document_name VARCHAR NOT NULL,
    stage VARCHAR,
    pages_parsed INT,
    total_pages INT,
    updated_on TIMESTAMP NULL,
);