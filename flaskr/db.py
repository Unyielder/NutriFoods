from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

engine = create_engine(r"sqlite:///C:\Users\Mohamed\PycharmProjects\Meal Prep\instance\Canadian_Foods.db", convert_unicode=True, echo=False)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

