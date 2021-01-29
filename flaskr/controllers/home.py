from flask import Blueprint, redirect, render_template, request, url_for
from flaskr.db import db_session
from flaskr.model import FoodName, ConversionFactor, MeasureName, NutrientAmount, NutrientName
from flask_login import login_required

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index', methods=('GET', 'POST'))
@login_required
def index():

    if request.method == 'POST':
        if request.form['btn'] == 'Search':
            return redirect(url_for('home.search'))

    return render_template('home/index.html')


@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    ingredient = f"{request.form['ingredient']}%"

    ing_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription)\
        .filter(FoodName.FoodDescription.like(ingredient)).all()

    if request.form['btn'] == 'Select':
        return redirect(url_for('home.serving', ingredient=ingredient))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('/serving', methods=('GET', 'POST'))
@login_required
def serving():
    food_id = request.form['ing_select']

    serving_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .filter(FoodName.FoodID == food_id).all()

    ing_title = serving_results[0][1]

    return render_template('home/serving.html', ing_title=ing_title, serving_results=serving_results)


