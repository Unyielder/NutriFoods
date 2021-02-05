from flask import Blueprint, redirect, render_template, request, url_for, session, jsonify
from flaskr.db import db_session
from flaskr.model import FoodName, ConversionFactor, MeasureName, NutrientAmount, NutrientName
from flask_login import login_required
from sqlalchemy import and_, func
from flaskr.business_logic.food import Food
from collections import defaultdict

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index', methods=('GET', 'POST'))
@login_required
def index():
    food_list = []
    session['food_list'] = food_list

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
        session['food_id'] = request.form['ing_select']
        return redirect(url_for('home.serving'))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('/serving', methods=('GET', 'POST'))
@login_required
def serving():
    food_id = session['food_id']

    serving_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .filter(FoodName.FoodID == food_id).all()

    food_name = serving_results[0][1]
    session['food_name'] = food_name

    if request.method == 'POST':
        session['ing_measure'] = request.form['ing_measure']
        return redirect(url_for('home.nutrients'))

    return render_template('home/serving.html', food_name=food_name, serving_results=serving_results)


@bp.route('/nutrients', methods=('GET', 'POST'))
@login_required
def nutrients():
    food_id = session['food_id']
    food_name = session['food_name']
    measure = session['ing_measure']

    ing_nutrients = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription,
                                     NutrientName.NutrientName,
                                     func.round((ConversionFactor.ConversionFactorValue * NutrientAmount.NutrientValue),
                                                2).label(
                                         'NutrientValCalc'),
                                     NutrientName.NutrientUnit) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .outerjoin(NutrientAmount, FoodName.FoodID == NutrientAmount.FoodID) \
        .outerjoin(NutrientName, NutrientAmount.NutrientID == NutrientName.NutrientID) \
        .filter(and_(NutrientName.NutrientCode.in_((208, 203, 204, 606, 291, 205)),
                     FoodName.FoodID == food_id, MeasureName.MeasureDescription == measure)).all()

    if request.method == 'POST':
        food = Food()
        food_list = session['food_list']

        food.load_food(ing_nutrients)
        food_list.append(food.__dict__)
        session['food_list'] = food_list

        return redirect(url_for('home.meal_prep'))

    return render_template('home/nutrients.html', ing_nutrients=ing_nutrients,
                           food_name=food_name,
                           measure=measure)


@bp.route('/meal_prep', methods=('GET', 'POST'))
@login_required
def meal_prep():
    macro_stats = defaultdict(list)
    meal = session['food_list']

    macro_stats['calories_total'] = sum([food['calories'][0] for food in meal])
    macro_stats['carbs_total'] = sum([food['carbs'][0] for food in meal])
    macro_stats['proteins_total'] = sum([food['proteins'][0] for food in meal])
    macro_stats['fats_total'] = sum([food['fat'][0] for food in meal])
    macro_stats['sat_fats_total'] = sum([food['sat_fat'][0] for food in meal])
    macro_stats['fiber_total'] = sum([food['fiber'][0] for food in meal])

    if request.method == 'POST':
        session['ingredient'] = f"{request.form['ingredient']}%"
        return redirect(url_for('home.search'))

    return render_template('home/meal_prep.html', meal=meal, macro_stats=macro_stats)
