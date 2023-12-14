from website import *


@app.route('/', methods=['GET', 'POST'])
def home_page():
    message = ''
    if flask_login.current_user():
        message = 'User id: ', flask_login.current_user()
    return render_template('home_page.html', message=message)
