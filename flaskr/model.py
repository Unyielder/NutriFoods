from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from flaskr.db import db_session


engine = create_engine(r"sqlite:///C:\Users\Mohamed\PycharmProjects\Meal Prep\instance\Canadian_Foods.db", convert_unicode=True, echo=False)

# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
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
    __tablename__= 'USER'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    UserName = Column(String, unique=True, nullable=False)
    PassWord = Column(String, nullable=False)
    Authenticated = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return '<User %r>' % self.username


Base.metadata.create_all(engine)

if __name__ == '__main__':


    """# testing addition of username and password in USERS table
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    food_id = 2003
    rs = db_session.query(FoodName.FoodID, FoodName.FoodDescription, MeasureName.MeasureDescription)\
        .outerjoin(ConversionFactor, FoodName.FoodID == ConversionFactor.FoodID)\
        .outerjoin(MeasureName, ConversionFactor.MeasureID == MeasureName.MeasureID)\
        .filter(FoodName.FoodID == food_id).all()
    for row in rs:
        print(row)

"""

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
