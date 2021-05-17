CREATE USER superset WITH PASSWORD 'superset123' CREATEDB;
CREATE DATABASE superset
    WITH
    OWNER = superset
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE USER airflow WITH PASSWORD 'airflow123' CREATEDB;

CREATE DATABASE airflow
    WITH
    OWNER = airflow
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
