from website import *


@app.route('/', methods=['GET', 'POST'])
def home_page():
    message = ''
    if flask_login.current_user.is_authenticated:
        message = 'User id: ', flask_login.get_id()
    return render_template('home_page.html', message=message)
