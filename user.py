import flask_login
from psycopg2 import errors
from database import database_access


class User:
    def __init__(self):
        self.user_id = -1
        self.username = ''
        self.password = ''
        self.name = ''
        self.surname = ''
        self.email = ''
        self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = True

    def create_new_user(self, username, password, name, surname, email):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
        self.is_active = True

    @database_access
    def add_user_to_db(self, conn, cursor):
        table_query = """
            INSERT INTO Account (username, password, name, surname, email)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (self.username, self.password, self.name, self.surname, self.email)
        try:
            cursor.execute(table_query, values)
            conn.commit()
        except errors.UniqueViolation:
            print("User with this email already exists.")
            conn.rollback()

    @staticmethod
    @database_access
    def authenticate_user(conn, cursor, username, password):
        from website import load_user
        table_query = """
            SELECT *
            FROM Account
            WHERE username = %s
            AND password = %s;
        """
        try:
            cursor.execute(table_query, (username, password))
            result = cursor.fetchall()[0][0]
            load_user(result)
            return True
        except IndexError:
            conn.rollback()
        return False

    @staticmethod
    @database_access
    def get(conn, cursor, user_id):
        table_query = """
            SELECT *
            FROM Account
            WHERE id = %s;
        """
        temp_user = User()
        try:
            cursor.execute(table_query, (user_id,))
            result = cursor.fetchall()[0]
            (
                temp_user.user_id,
                temp_user.username,
                temp_user.password,
                temp_user.name,
                temp_user.surname,
                temp_user.email,
                temp_user.is_active
            ) = result
            temp_user.is_authenticated = True
            temp_user.is_anonymous = False
            return temp_user
        except IndexError:
            conn.rollback()
            return None

    def get_id(self):
        return str(self.user_id)

    @staticmethod
    def logout():
        flask_login.logout_user()
