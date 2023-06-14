DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'heissdocs') THEN
        CREATE DATABASE heissdocs;
    END IF;
END
$$;
SELECT pg_sleep(5);