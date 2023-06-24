CREATE TABLE IF NOT EXISTS settings (
	id VARCHAR PRIMARY KEY,
	user_email VARCHAR unique not null,
	aws_access_key VARCHAR,
	aws_secret VARCHAR,
	aws_region VARCHAR,
	no_sql_provider VARCHAR,
	document_table_name VARCHAR,
	parsing_api_key VARCHAR,
	buckets_list VARCHAR,
	scan_bucket VARCHAR
);
