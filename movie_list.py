from website import *
from database import database_access


@database_access
def get_movies(conn, cursor):
    table_query = """
                SELECT *
                FROM movie;
            """
    try:
        cursor.execute(table_query)
        result = cursor.fetchall()
        return result
    except IndexError:
        conn.rollback()


@app.route('/movie_list', methods=["GET", "POST"])
def movie_list():
    if request.method == "GET":
        movies = get_movies()
        return render_template('movie_list.html', movies=movies)
    elif request.method == "POST":
        return render_template('movie_list.html')
