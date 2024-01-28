import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Crear una conexión a la base de datos SQLite especificada por db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """Crear una tabla desde la sentencia create_table_sql."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "RecruitmentToolDB.sqlite"

    sql_create_candidates_table = """
    CREATE TABLE IF NOT EXISTS candidates (
        id integer PRIMARY KEY,
        name text NOT NULL,
        email text NOT NULL,
        education text,
        experience text
    );
    """

    sql_create_positions_table = """
    CREATE TABLE IF NOT EXISTS positions (
        id integer PRIMARY KEY,
        title text NOT NULL,
        description text,
        requirements text
    );
    """

    # Crear una conexión a la base de datos
    conn = create_connection(database)

    # Crear tablas
    if conn is not None:
        # Crear tabla de candidatos
        create_table(conn, sql_create_candidates_table)

        # Crear tabla de posiciones
        create_table(conn, sql_create_positions_table)
    else:
        print("Error! No se puede crear la conexión a la base de datos.")

if __name__ == '__main__':
    main()
