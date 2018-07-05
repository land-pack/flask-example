from flask import render_template, Blueprint

# config
users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register')
def user_register():
    return render_template('register.html')


@users_blueprint.route('/login')
def user_login():
    return render_template('login.html')


@users_blueprint.route('/logout')
def user_logout():
    return render_template('logout.html')
