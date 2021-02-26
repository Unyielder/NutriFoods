from flask import Blueprint, redirect, render_template, request, url_for, session
from flaskr.db import db_session
from flaskr.model import FoodName, ConversionFactor, MeasureName, NutrientAmount, NutrientName
from sqlalchemy import and_, func
from flaskr.business_logic.food import Food
from collections import defaultdict

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/', methods=('GET', 'POST'))
def index():
    # Initializes food group variables for group analysis
    food_list = []
    food_list2 = []
    session['food_list'] = food_list
    session['food_list2'] = food_list2

    return render_template('home/index.html')


@bp.route('/food_query', methods=('GET', 'POST'))
def food_query():
    if request.method == 'POST':
        ingredient = request.form.get('ingredient')
        return redirect(url_for('home.sch_q', ingredient=ingredient))

    return render_template('home/food_query.html')


@bp.route('sch_q/search/<ingredient>', methods=('GET', 'POST'), endpoint='sch_q')
@bp.route('sch_c1/search/<ingredient>', methods=('GET', 'POST'), endpoint='sch_c1')
@bp.route('sch_c2/search/<ingredient>', methods=('GET', 'POST'), endpoint='sch_c2')
def search(ingredient):
    ing_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription) \
        .filter(FoodName.FoodDescription.like(f'{ingredient}%')).all()

    if request.method == 'POST':
        food_id = request.form['ing_select']
        session['food_id'] = food_id

        if 'sch_q' in request.path:
            return redirect(url_for('home.ser_q', food_id=food_id))
        elif 'sch_c1' in request.path:
            return redirect(url_for('home.ser_c1', food_id=food_id))
        elif 'sch_c2' in request.path:
            return redirect(url_for('home.ser_c2', food_id=food_id))

    return render_template('home/search.html', ing_results=ing_results)


@bp.route('ser_q/serving/<int:food_id>', methods=('GET', 'POST'), endpoint='ser_q')
@bp.route('ser_c1/serving/<int:food_id>', methods=('GET', 'POST'), endpoint='ser_c1')
@bp.route('ser_c2/serving/<int:food_id>', methods=('GET', 'POST'), endpoint='ser_c2')
def serving(food_id):
    serving_results = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .filter(FoodName.FoodID == food_id).all()

    food_name = serving_results[0][1]
    session['food_name'] = food_name

    if request.method == 'POST':
        measure = request.form['ing_measure']


        #session['checked'] = []
        #for checkbox in 'macros', 'vitamins', 'minerals', 'amino_acids', 'steroids', 'misc':
        #    value = request.form.get(checkbox)
        #    if value:
        #        session['checked'].append(value)

        if 'ser_q' in request.path:
            return redirect(url_for('home.nut_q', food_id=food_id, measure=measure))
        elif 'ser_c1' in request.path:
            return redirect(url_for('home.nut_c1', food_id=food_id, measure=measure))
        elif 'ser_c2' in request.path:
            return redirect(url_for('home.nut_c2', food_id=food_id, measure=measure))

    return render_template('home/serving.html', food_name=food_name, serving_results=serving_results)


def nutrient_query(nutrient_codes, food_id, measure):
    res = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription,
                                 NutrientName.NutrientName,
                                 func.round((ConversionFactor.ConversionFactorValue * NutrientAmount.NutrientValue),
                                            2).label(
                                     'NutrientValCalc'),
                                 NutrientName.NutrientUnit) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .outerjoin(NutrientAmount, FoodName.FoodID == NutrientAmount.FoodID) \
        .outerjoin(NutrientName, NutrientAmount.NutrientID == NutrientName.NutrientID) \
        .filter(and_(NutrientName.NutrientCode.in_(nutrient_codes),
                     FoodName.FoodID == food_id, MeasureName.MeasureDescription == measure)).all()
    return res


def load_food(food_id, measure):
    food = Food()

    macro_codes = (208, 203, 204, 606, 291, 205)
    res = nutrient_query(macro_codes, food_id, measure)
    food.load_macros(res)

    vit_codes = (
        430, 573, 323, 341, 342,
        343, 325, 324, 328, 401,
        435, 410, 415, 418, 578,
        416, 404, 409, 406, 405,
        417, 432, 431, 320, 319,
        322)
    res = nutrient_query(vit_codes, food_id, measure)
    food.load_vitamins(res)

    mineral_codes = (
        301, 317, 306, 303,
        315, 304, 312, 309
    )
    res = nutrient_query(mineral_codes, food_id, measure)
    food.load_minerals(res)

    amino_codes = (
        510, 509, 501, 502, 263,
        517, 518, 508, 513, 514,
        550, 504, 505, 503, 521,
        512, 516, 515, 506, 507,
        511, 203
    )
    res = nutrient_query(amino_codes, food_id, measure)
    food.load_aminos(res)

    steroid_codes = (
        639, 638, 641, 636, 601
    )
    res = nutrient_query(steroid_codes, food_id, measure)
    food.load_steroids(res)

    misc_codes = (
        305, 245, 255, 337, 338,
        421, 262, 454, 334, 321,
        207, 221
    )
    res = nutrient_query(misc_codes, food_id, measure)
    food.load_misc(res)

    return food


@bp.route('nut_q/nutrients/<int:food_id>/<measure>', methods=('GET', 'POST'), endpoint='nut_q')
@bp.route('nut_c1/nutrients/<int:food_id>/<measure>', methods=('GET', 'POST'), endpoint='nut_c1')
@bp.route('nut_c2/nutrients/<int:food_id>/<measure>', methods=('GET', 'POST'), endpoint='nut_c2')
def nutrients(food_id, measure):
    food_name = session['food_name']

    food = load_food(food_id, measure)

    food.id = food_id
    food.name = food_name
    food.measure = measure

    if request.method == 'POST':
        if 'nut_c1' in request.path:
            food = load_food(food_id, measure)

            food_list = session['food_list']
            food_list.append(food.__dict__)
            session['food_list'] = food_list

            return redirect(url_for('home.food_compare'))

        elif 'nut_c2' in request.path:
            food_2 = load_food(food_id, measure)

            food_list2 = session['food_list2']
            food_list2.append(food_2.__dict__)
            session['food_list2'] = food_list2

            return redirect(url_for('home.food_compare'))

    return render_template('home/nutrients.html', food=food,
                           food_name=food_name,
                           measure=measure,
                           request=request)


@bp.route('/food_compare', methods=('GET', 'POST'))
def food_compare():
    macro_stats = defaultdict(list)
    macro_stats_2 = defaultdict(list)
    meal = session['food_list']
    meal_2 = session['food_list2']

    macro_stats['calories_total'] = sum([food['calories'][0] for food in meal])
    macro_stats['carbs_total'] = sum([food['carbs'][0] for food in meal])
    macro_stats['proteins_total'] = sum([food['proteins'][0] for food in meal])
    macro_stats['fats_total'] = sum([food['fat'][0] for food in meal])
    macro_stats['sat_fats_total'] = sum([food['sat_fat'][0] for food in meal])
    macro_stats['fiber_total'] = sum([food['fiber'][0] for food in meal])

    macro_stats_2['calories_total'] = sum([food['calories'][0] for food in meal_2])
    macro_stats_2['carbs_total'] = sum([food['carbs'][0] for food in meal_2])
    macro_stats_2['proteins_total'] = sum([food['proteins'][0] for food in meal_2])
    macro_stats_2['fats_total'] = sum([food['fat'][0] for food in meal_2])
    macro_stats_2['sat_fats_total'] = sum([food['sat_fat'][0] for food in meal_2])
    macro_stats_2['fiber_total'] = sum([food['fiber'][0] for food in meal_2])

    if request.method == 'POST':
        if request.form.get("addButton1"):
            ingredient = f"{request.form['ingredient']}%"
            return redirect(url_for('home.sch_c1', ingredient=ingredient))

        if request.form.get("addButton2"):
            ingredient = f"{request.form['ingredient2']}%"
            session['ingredient_2'] = ingredient
            return redirect(url_for('home.sch_c2', ingredient=ingredient))

    return render_template('home/food_compare.html', meal=meal, meal_2=meal_2,
                           macro_stats=macro_stats, macro_stats_2=macro_stats_2)


@bp.route('/delete_item/<int:food_id>', methods=('GET', 'POST'))
def delete_group_1(food_id):
    meal = session['food_list']
    meal = [food for food in meal if food['id'] != food_id]
    session['food_list'] = meal

    return redirect(url_for('home.food_compare'))


@bp.route('/delete_item2/<int:food_id>', methods=('GET', 'POST'))
def delete_group_2(food_id):
    meal_2 = session['food_list2']
    meal_2 = [food for food in meal_2 if food['id'] != food_id]
    session['food_list2'] = meal_2

    return redirect(url_for('home.food_compare'))
