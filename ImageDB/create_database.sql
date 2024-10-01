DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'ImageDB') THEN
        CREATE DATABASE ImageDB;
    END IF;
END $$;