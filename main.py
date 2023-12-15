from user import User
from login import login
from home_page import home_page
from logout import logout
from movie_list import movie_list, get_movies
from website import *

user = User()

if __name__ == '__main__':
    app.run(debug=True)
