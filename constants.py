import environment as E


DATABASE_CONFIG = {
    "dbname": E.DB_NAME_,
    "user": E.DB_USER_,
    "password": E.DB_PASSWORD_,
    "host": E.DB_HOST_,
    "port": E.DB_PORT_
}

QUERY = "SELECT COUNT(*) FROM gdp_per_capita"

TABLE_CREATION_QUERY = """
CREATE TABLE IF NOT EXISTS gdp_per_capita (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100),
    year INT,
    gdp_per_capita FLOAT
)
"""

INSERT_QUERY = """
INSERT INTO gdp_per_capita (country, year, gdp_per_capita) VALUES (%s, %s, %s)
"""
