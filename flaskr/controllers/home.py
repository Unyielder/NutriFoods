from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flaskr.db import get_db
from flaskr.business_logic.queries import Queries

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        if request.form['btn'] == 'Search':
            return redirect(url_for('home.search'))

    return render_template('home/index.html')


@bp.route('/search', methods=('GET', 'POST'))
def search():
    ingredient = request.form['ingredient']
    ing_query = Queries(ingredient)
    db = get_db()

    ing_results = db.execute(ing_query.ingredient_query).fetchall()

    if request.form['btn'] == 'Add':
        return redirect(url_for('home.serving'))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('/serving', methods=('GET', 'POST'))
def serving():
    ing_select = request.form['ing_select']
    serving_query = Queries(ing_select)
    db = get_db()

    serving_results = db.execute(serving_query.measures_query).fetchall()
    ing_title = serving_results[0][1]

    return render_template('home/serving.html', ing_title=ing_title, serving_results=serving_results)
