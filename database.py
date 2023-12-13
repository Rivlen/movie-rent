import psycopg2


class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def create_conn_cursor(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor
        except psycopg2.OperationalError as err:
            raise err

    def close_conn_cursor(self):
        self.cursor.close()
        self.conn.close()
