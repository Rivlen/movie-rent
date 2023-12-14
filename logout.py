from website import *


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect('/')
