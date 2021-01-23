from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///../instance/Canadian_Foods.db", convert_unicode=True, echo=False)

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Users = Base.classes.USERS
MeasureName = Base.classes.MEASURE_NAME
ConversionFactor = Base.classes.CONVERSION_FACTOR
FoodGroup = Base.classes.FOOD_GROUP
FoodSource = Base.classes.FOOD_SOURCE
FoodName = Base.classes.FOOD_NAME
YieldName = Base.classes.YIELD_NAME
#YieldAmount = Base.classes.YIELD_AMOUNT
#NutrientAmount = Base.classes.NUTRIENT_AMOUNT
NutrientName = Base.classes.NUTRIENT_NAME
NutrientSource = Base.classes.NUTRIENT_SOURCE

# testing addition of username and password in USERS table
session = Session(engine)
session.add(Users(UserName="test username2", PassWord="test password2"))
session.commit()


"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
Base.metadata.reflect(engine)


class Users(Base):
    __table__ = Base.metadata.tables['USERS']


class MeasureName(Base):
    __table__ = Base.metadata.tables['MEASURE_NAME']


class ConversionFactor(Base):
    __table__ = Base.metadata.tables['CONVERSION_FACTOR']


class FoodGroup(Base):
    __table__ = Base.metadata.tables['FOOD_GROUP']


class FoodSource(Base):
    __table__ = Base.metadata.tables['FOOD_SOURCE']


class FoodName(Base):
    __table__ = Base.metadata.tables['FOOD_NAME']
    food_ids = relationship("YieldName", backref="FoodName")


class YieldName(Base):
    __table__ = Base.metadata.tables['YIELD_NAME']


class YieldAmount(Base):
    __table__ = Base.metadata.tables['YIELD_AMOUNT']


class NutrientAmount(Base):
    __table__ = Base.metadata.tables['NUTRIENT_AMOUNT']


class NutrientName(Base):
    __table__ = Base.metadata.tables['NUTRIENT_NAME']


class NutrientSource(Base):
    __table__ = Base.metadata.tables['NUTRIENT_SOURCE']

"""
