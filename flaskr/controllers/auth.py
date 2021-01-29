import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, abort
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import db_session
from flaskr.model import User
from flask_login import login_user, logout_user

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db_session.query(User.id).filter(User.UserName == username).first() is not None:
            error = f'User {username} is already registered.'

        if error is None:
            user = User(UserName=username, PassWord=generate_password_hash(password))
            db_session.add(user)
            db_session.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = db_session.query(User).filter(User.UserName == username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.PassWord, password):
            error = 'Incorrect password.'

        if error is None:
            user.Authenticated = 1
            db_session.commit()
            login_user(user)
            # session.clear()
            session['user_id'] = user.id
            session['user'] = username

            flash('Logged in successfully.')
            next = request.args.get('next')

            #if not is_safe_url(next):
            #    return abort(400)

            return redirect(url_for('home.index'))

        flash(error)

    return render_template('auth/login.html', session=session)


@bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
