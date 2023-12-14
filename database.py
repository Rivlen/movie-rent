import psycopg2


def create_conn_cursor(host, database, user, password):
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        return conn, cursor
    except psycopg2.OperationalError as err:
        raise err


def close_conn_cursor(conn, cursor):
    cursor.close()
    conn.close()


def database_access(func):
    def wrapper(*args, **kwargs):
        db = (
            "localhost",
            "movierentdb",
            "postgres",
            "password"
        )
        conn, cursor = create_conn_cursor(*db)
        try:
            result = func(conn, cursor, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            close_conn_cursor(conn, cursor)

    return wrapper
