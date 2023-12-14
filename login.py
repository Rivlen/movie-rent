from website import *


@app.route('/login', methods=["GET", "POST"])
def login():
    error = ''
    if request.method == "GET":
        return render_template('login_page.html', error=error)
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if User.authenticate_user(username, password):
            return redirect('/')
        error = 'Username or password not valid'
        return render_template('login_page.html', error=error)
