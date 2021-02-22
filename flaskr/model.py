from sqlalchemy import create_engine, Column, Integer, String, and_, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

from flaskr.db import db_session

engine = create_engine(r"sqlite:///C:\Users\Mohamed\PycharmProjects\Meal Prep\instance\Canadian_Foods.db",
                       convert_unicode=True, echo=False)

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default

MeasureName = Base.classes.MEASURE_NAME
ConversionFactor = Base.classes.CONVERSION_FACTOR
FoodGroup = Base.classes.FOOD_GROUP
FoodSource = Base.classes.FOOD_SOURCE
FoodName = Base.classes.FOOD_NAME
YieldName = Base.classes.YIELD_NAME
YieldAmount = Base.classes.YIELD_AMOUNT
NutrientAmount = Base.classes.NUTRIENT_AMOUNT
NutrientName = Base.classes.NUTRIENT_NAME
NutrientSource = Base.classes.NUTRIENT_SOURCE

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base, UserMixin):
    __tablename__ = 'USER'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    UserName = Column(String, unique=True, nullable=False)
    PassWord = Column(String, nullable=False)
    Authenticated = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return '<User %r>' % self.username


# Base.metadata.create_all(engine)

if __name__ == '__main__':

    food_id = 2

    # Vitamins
    nut_codes = (
        430, 573, 323, 341, 342,
        343, 325, 324, 328, 401,
        435, 410, 415, 418, 578,
        416, 404, 409, 406, 405,
        417, 432, 431, 320, 319,
        322)

    # Minerals
    nut_codes = (
        301, 317, 306, 303, 315,
        304, 312, 309
    )

    # Amino-acids
    nut_codes = (
        510, 509, 501, 502, 263,
        517, 518, 508, 513, 514,
        550, 504, 505, 503, 521,
        512, 516, 515, 506, 507,
        511, 203
    )

    # Cholesterol
    nut_codes = (
        639, 638, 641, 636, 601
    )

    # Misc
    nut_codes = (
        305, 245, 255, 337, 338,
        421, 262, 454, 334, 321,
        207, 221
    )

    rs = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription,
                          NutrientName.NutrientName,
                          func.round((ConversionFactor.ConversionFactorValue * NutrientAmount.NutrientValue), 2).label(
                              'NutrientValCalc'),
                          NutrientName.NutrientUnit) \
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID) \
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID) \
        .outerjoin(NutrientAmount, FoodName.FoodID == NutrientAmount.FoodID) \
        .outerjoin(NutrientName, NutrientAmount.NutrientID == NutrientName.NutrientID) \
        .filter(and_(NutrientName.NutrientCode.in_(nut_codes),
                     FoodName.FoodID == 2, MeasureName.MeasureDescription == '100ml')).all()

    for row in rs:
        print(row)
