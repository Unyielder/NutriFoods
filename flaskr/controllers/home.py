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
        ingredient = request.form.get('ingredient')
        return redirect(url_for('home.search', ingredient=ingredient))

    return render_template('home/index.html')


@bp.route('/search/<ingredient>', methods=('GET', 'POST'))
@login_required
def search(ingredient):

    ing_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription) \
        .filter(FoodName.FoodDescription.like(f'{ingredient}%')).all()

    if request.method == 'POST':
        food_id = request.form['ing_select']
        session['food_id'] = food_id

        return redirect(url_for('home.serving', food_id=food_id))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('/serving/<int:food_id>', methods=('GET', 'POST'))
@login_required
def serving(food_id):

    serving_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .filter(FoodName.FoodID == food_id).all()

    food_name = serving_results[0][1]
    session['food_name'] = food_name

    if request.method == 'POST':
        measure = request.form['ing_measure']
        session['ing_measure'] = measure

        return redirect(url_for('home.nutrients', food_id=food_id, measure=measure))

    return render_template('home/serving.html', food_name=food_name, serving_results=serving_results)


@bp.route('/nutrients/<int:food_id>/<measure>', methods=('GET', 'POST'))
@login_required
def nutrients(food_id, measure):
    food_name = session['food_name']

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
        ingredient = f"{request.form['ingredient']}%"
        session['ingredient'] = ingredient
        return redirect(url_for('home.search', ingredient=ingredient))

    return render_template('home/meal_prep.html', meal=meal, macro_stats=macro_stats)


@bp.route('/delete_item/<int:food_id>', methods=('GET', 'POST'))
@login_required
def delete_item(food_id):
    meal = session['food_list']

    meal = [food for food in meal if food['id'] != food_id]
    session['food_list'] = meal

    return redirect(url_for('home.meal_prep'))

@bp.route('/save_meal', methods=('GET', 'POST'))
@login_required
def save_meal():
    pass
