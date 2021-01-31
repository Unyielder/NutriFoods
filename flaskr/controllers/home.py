from flask import Blueprint, redirect, render_template, request, url_for, session
from flaskr.db import db_session
from flaskr.model import FoodName, ConversionFactor, MeasureName, NutrientAmount, NutrientName
from flask_login import login_required
from sqlalchemy import and_, func
from flaskr.business_logic import food

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        session['ingredient'] = f"{request.form['ingredient']}%"
        return redirect(url_for('home.search'))

    return render_template('home/index.html')


@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    ingredient = session['ingredient']

    ing_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription) \
        .filter(FoodName.FoodDescription.like(ingredient)).all()

    if request.method == 'POST':
        session['ing_select'] = request.form['ing_select']
        return redirect(url_for('home.serving'))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('/serving', methods=('GET', 'POST'))
@login_required
def serving():
    food_id = session['ing_select']

    serving_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .filter(FoodName.FoodID == food_id).all()

    ing_title = serving_results[0][1]

    if request.method == 'POST':
        session['ing_measure'] = request.form['ing_measure']
        return redirect(url_for('home.nutrients'))

    return render_template('home/serving.html', ing_title=ing_title, serving_results=serving_results)


@bp.route('/nutrients', methods=('GET', 'POST'))
@login_required
def nutrients():
    food_id = session['ing_select']
    measure = session['ing_measure']

    ing_nutrients = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription,
                                     NutrientName.NutrientName,
                                     func.round((ConversionFactor.ConversionFactorValue * NutrientAmount.NutrientValue), 2).label(
                                         'NutrientValCalc'),
                                     NutrientName.NutrientUnit) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .outerjoin(NutrientAmount, FoodName.FoodID == NutrientAmount.FoodID) \
        .outerjoin(NutrientName, NutrientAmount.NutrientID == NutrientName.NutrientID) \
        .filter(and_(NutrientName.NutrientCode.in_((208, 203, 204, 606, 291, 205)),
                     FoodName.FoodID == food_id, MeasureName.MeasureDescription == measure)).all()

    return render_template('home/nutrients.html', ing_nutrients=ing_nutrients)
